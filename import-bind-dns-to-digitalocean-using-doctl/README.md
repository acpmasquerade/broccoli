# Story
- I was moving the DNS management around different providers, and once had to import to Digital Ocean
- DO provides free DNS service for its customers
- The earlier provider had allowed to export the records in BIND format.

# Usage
- ```python3 script.py zonefile.txt exampledomain.com > do_script.sh```
- ```bash do_script.sh```

# What does it do ?
- Parse the DNS records in file
- Checks if the record matches a valid DNS record template
  ```<ALIAS> <TTL> IN <RecordTYPE> <VALUE>```
- Creates Digital Ocean Script commands for the DO supported DNS records



