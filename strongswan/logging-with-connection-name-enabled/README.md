# Enable Connection name (IKE name) while charon logging daemon logs in strongswan

- keep all settings default
- keep logging level 1 atleast (for more sensible output)
- define a custom logging identifier
- enable ike_name in settings

## Config file
/etc/strongswan.d/charon-logging.conf

## Effective config
```
syslog {
        daemon {
          default = 1
          ike_name = yes
        }
    }
```

## Modified Logs
```
Feb  5 11:38:14 broccoliserver 'vpnlogs': 11[NET] <telcovpn|4> sending packet: from 100.100.100.100[500] to 200.200.200.200[500] (92 bytes)
..
..
..
```
