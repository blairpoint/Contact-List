#!/bin/bash

        CONTACTS="contacts.txt"

        echo -n "Name to search: "
        read find

        echo "Name "
        grep -i $find $CONTACTS
read null
