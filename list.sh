#!/bin/sh
clear
CONTACTS="contacts.txt"

echo "Name | Phone | Email"


cut -d ";" -f 1,2,3 $CONTACTS

        echo "Would you like to view a contact?"
        echo -n "y/n: "
        read response
        if [ "$response" = "y" ]
        then
		./search.sh
	else
		./contactlist.sh
		#read null
        fi


