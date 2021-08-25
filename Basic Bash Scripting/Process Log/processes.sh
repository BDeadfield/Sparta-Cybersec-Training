# Create 'processes' directory and clear console log

mkdir processes
clear

# Continuously loop (until the user exits)

while true
do

# Asign a file path based on time / date

   DIRECTORY="processes/"$(date +"%F-%T").log

# Create a log file at said file path and fill it with the system's currently running processes every 30 seconds

   touch $DIRECTORY
   ps -e > $DIRECTORY

   sleep 30

done
