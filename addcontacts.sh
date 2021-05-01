   #!/bin/sh

        CONTACTS="contacts.txt"

        echo -n "Contact name: " 
        read name

        echo -n "Phone #: "
        read ph

	echo -n "Email address: "
	read email		

	echo -n "Street address: "
	read addr        

	echo -n "Suburb: "
	read sub

	echo -n "City: "
	read city

	
	echo "Are you sure you want to add this contact?"
        echo -e "$name \n $ph \n $email \n $addr \n $sub \n $city \n"
        echo -n "y/n: "
        read response

        if [ "$response" == "y" ] 
        then
            echo "$name ; $ph ; $email ; $addr ; $sub ; $city" >>$CONTACTS
	    echo "$CONTACTS updated"

        else
            echo "$name contact not saved"
        fi
read null
        exit 0

