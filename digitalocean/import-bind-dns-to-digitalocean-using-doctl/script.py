# Story
# - I was moving the DNS management around different providers, and once had to import to Digital Ocean
# - DO provides free DNS service for its customers
# - The earlier provider had allowed to export the records in BIND format.

# Usage
# python3 script.py zonefile.txt exampledomain.com

import sys
import re

try:
    srcfile = sys.argv[1]
except IndexError:
    sys.exit("# Error ! Missing Argument - filename")

try:
    domain = sys.argv[2]
except IndexError:
    print("# !! Domain not specified. Using example.com")
    domain = "example.com"

supported_types = ['A','AAAA','CNAME','MX','TXT','NS','SRV','CAA']
dns_record_re = re.compile(r'(?P<alias>[^\s]+)\s+(?P<ttl>\d+)\s+IN\s+(?P<rtype>[^\s]+)\s+(?P<value>.*)$')
mx_re = re.compile(r'(?P<priority>\d+)\s+(?P<value>.*)')

def parse_dns_record(record):
    re_match = dns_record_re.match(record)
    if re_match:
        rtype = re_match.group('rtype')
        if rtype not in supported_types:
            print("#", record, "# -- Skipped !! - Not a supported record type\n")
            return False, False, False, False
        
        alias = re_match.group('alias')
        ttl = re_match.group('ttl')
        value = re_match.group('value')

        print("#", rtype, ttl, alias, value)
        return rtype, ttl, alias, value
    else:
        print("#", record, "# -- Skipped !! - Not a valid DNS record\n")
        return False, False, False, False

try:
    do_command = "doctl compute domain records create"
    with open(srcfile, "r") as fp:
        doctl_commands = []
        for record in fp.readlines():
            rtype, ttl, alias, value = parse_dns_record(record)
            if rtype is False:
                continue

            priority = 0
            record_data = value

            if rtype == "MX":
                mx_matches = mx_re.match(value)
                priority = mx_matches.group('priority')
                record_data = mx_matches.group('value')
                
            cmd = f"{do_command} {domain} --record-priority={priority} --record-type={rtype} --record-name={alias} --record-ttl={ttl} --record-data={record_data}"
            
            doctl_commands.append(cmd)

        print("# --- doctl commands start from here .... ")
        for cmd in doctl_commands:
            print(cmd )
except IOError:
    sys.exit("# Error ! Failed to open the file")
    
   
