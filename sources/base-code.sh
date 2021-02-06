#!/bin/bash

# Variabelen
root="/home/jeroen/docker/"
destination="/home/jeroen/backup-docker"
filter="merge /home/jeroen/filter-docker.txt"
succeeded_message="Backup geslaagd"
failed_message="Backup mislukt"
dateformat=$(date +"%Y-%m-%d")
logfile="/home/jeroen/docker/docker-logs"

# Maak de backup
# rsync -zrlct --stats --delete --no-o --no-g --no-perms --omit-dir-times -f="merge /home/jeroen/filter.txt" /home/jeroen/mineser/ /home/jeroen/mine-nas/backup/survival/1.15
rsync -zrlctq --stats --delete --no-o --no-t --no-g --no-perms --omit-dir-times -K -L -f="$filter" "$root" "$destination"

if [ "$?" -eq "0" ]
then
  echo $(date) >> $logfile/$dateformat.log
  echo "$succeeded_message" >> $logfile/$dateformat.log
  echo "$root >> $destination" >> $logfile/$dateformat.log
  echo " " >> $logfile/$dateformat.log
else
  # Log de output naar /home/jeroen/mineser/mineser-logs
  echo $(date) >> $logfile/$dateformat.log
  echo "$failed_message" >> $logfile/$dateformat.log
  echo "Rsync error code $?" >> $logfile/$dateformat.log
  echo "Check error codes at https://linux.die.net/man/1/rsync" >> $logfile/$dateformat.log
  echo "$root >> $destination" >> $logfile/$dateformat.log
  echo " " >> $logfile/$dateformat.log
fi
