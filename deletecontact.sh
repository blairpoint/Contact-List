#!/bin/bash

CONTACTS="contacts.txt"
CONTEMP="contemp.txt"

echo -n "Which contact do you want to delete? "
read con2del

    echo "Are you sure you want to delete contact: $con2del ?"
        echo -n "y/n: "
        read response                                                                                     
        if [ "$response" == "y" ]
        then
	    cat $CONTACTS | grep -v $con2del>$CONTEMP
	    mv $CONTEMP $CONTACTS
            echo "Contact $con2del deleted from contact list"

        else
            echo "$con2del not deleted"
        fi
read null
        exit 0
