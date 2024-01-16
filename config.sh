#!/bin/bash
echo # add white space for formatting

echo "Configuring Git..."
echo "-----------------------------------------"
# config username and print for confirmation
echo "User: $(grep User credentials.txt | cut -d : -f 2)"
grep User credentials.txt | cut -d : -f 2 | git config --global user.name
# config email and print for confirmation
echo "Email: $(grep Email credentials.txt | cut -d : -f 2)" 
grep Email credentials.txt | cut -d : -f 2 | git config --global user.email
echo # add white space for formatting

echo "Displaying OS Info..."
echo "-----------------------------------------"
cat /etc/os-release
echo # add white space for formatting