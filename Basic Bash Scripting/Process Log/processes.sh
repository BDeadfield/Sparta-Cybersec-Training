mkdir processes
clear

while true
do

   DIRECTORY="processes/"$(date +"%F-%T").log

   touch $DIRECTORY
   ps -e > $DIRECTORY

   sleep 30

done
