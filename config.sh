#!/bin/ash
echo "" # add white space for formatting

echo "Configuring Git..."
echo "-----------------------------------------"
# config username and print for confirmation
echo -n "User: " 
cat credentials.txt | grep User | cut -d : -f 2 | git config --global user.name
# config email and print for confirmation
echo -n "Email: " 
cat credentials.txt | grep Email | cut -d : -f 2 | git config --global user.email
echo "" # add white space for formatting

echo "Displaying OS Info..."
echo "-----------------------------------------"
cat /etc/os-release
echo "" # add white space for formatting