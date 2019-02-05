# Enable Connection name (IKE name) while charon logging daemon logs in strongswan

- keep all settings default
- keep logging level 1 atleast (for more sensible output)
- define a custom logging identifier
- enable ike_name in settings

# Config file
/etc/strongswan.d/charon-logging.conf

# Effective config
```
syslog {
        daemon {
          default = 1
          ike_name = yes
        }
    }
```
    
