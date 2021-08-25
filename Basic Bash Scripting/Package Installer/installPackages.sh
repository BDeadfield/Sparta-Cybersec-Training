# Requests and stores username, password, directory and number of packages the user wishes to install

echo "Please enter a username:"
read USERNAME

# Uses -s to prevent text being displayed in console (silent prompt)

echo "Please enter a password:"
read -s PASSWORD

echo "Please enter a directory:"
read DIRECTORY

echo "Please enter the number of packages you would like to install:"
read PACKAGE_NUMBER

# Prints the directory the user is currently working from

echo "The current working directory is: " $(pwd)

# Creates new directory and log file based on prior user input

mkdir $DIRECTORY

touch $DIRECTORY/cyber.log

# Prints current working directory, user, date, selected username / password and the number of packages to be installed

echo "The current working directory is: " $(pwd) > $DIRECTORY/cyber.log

echo "The current user is: " $(whoami) >> $DIRECTORY/cyber.log

echo "The date is: " $(date) >> $DIRECTORY/cyber.log

echo "The selected username is: " $USERNAME >> $DIRECTORY/cyber.log

echo "The selected password is: " $PASSWORD >> $DIRECTORY/cyber.log

echo "The number of packages you would like to install is: "$PACKAGE_NUMBER >> $DIRECTORY/cyber.log

# Creates folder for individual package logs

mkdir $DIRECTORY/logs

# Adds another line to cyber.log in preparation for new lines listing packages

echo "The packages you have selected to install are: " >> $DIRECTORY/cyber.log

# Updates list of package updates available and clears terminal log

sudo apt-get update
clear

# For the amount of packages the user requested to install, the script will request a package name, add it's name to cyber.log, create a new file for installation logging in the logs folder, install requested package whilst pipelining logs to said log file, and then finally, clearing the terminal before exiting.

for x in $( seq $PACKAGE_NUMBER )
do
   echo "Please enter a package to install: "
   read
   echo ${REPLY} >> $DIRECTORY/cyber.log
   touch $DIRECTORY/logs/${REPLY}.log
   sudo apt-get install ${REPLY} -y > $DIRECTORY/logs/${REPLY}.log
   clear
done
