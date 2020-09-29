`innodb_log_group_home_dir=`

This parameter in the mysql config defines the location of `ib_logfile0` and `ib_logfile1` which defaults to the mysql datadir.

If the file size for these log files is configured to be say 4G - then the files take 8G of disk space. 

Moving these files to a separate directory / drive can save the datadir space for immediate requirements.

PS : Ubuntu systems might require to fix the apparmor settings. For eg. if `/var/log/mysql-innologs/` is the new directory, need to add these two lines in the apparmor file

### apparmor config file - 
`/etc/apparmor.d/usr.sbin.mysqld`

### Lines added
```
  /var/log/mysql-innologs/ r,
  /var/log/mysqlinnologs/** rwk,
```
