#!/bin/bash
clear

        CONTACTS="contacts.txt"

        exit=0

        while [ $exit -ne 1 ]
        do
            echo "Enter selection: "
            echo -e " [a] add"
	    echo -e " [l] list"
	    echo -e " [s] search"
	    echo -e " [m] modify"
	    echo -e " [d] delete"
	    echo -e " [x] exit "
            read response

            if [ "$response" = "a" ]
            then
                ./addcontacts.sh
            elif [ "$response" = "l" ]
            then
                ./list.sh
            elif [ "$response" = "s" ]
            then
                ./search.sh
	    elif [ "$response" = "m" ]
	    then
		./modifycontact.sh
            elif [ "$response" = "d" ]
            then
                ./deletecontact.sh
            elif [ "$response" = "x" ]
            then
                exit=1
            else
                echo "Invalid command"
            fi
	clear
        done

        exit 0
