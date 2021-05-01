#!/bin/bash

CONTACTS="contacts.txt"
CONTEMP="contemp.txt"

echo -n "Which contact do you want to modify? "
read con2mod

echo -n "Which field to you want to change? "
echo -n "[n] Name: "
echo -n "[p] Phone: "
echo -n "[e] Email address: "
echo -n "[a] Street Address: "
echo -n "[s] Suburb: "
echo -n "[c] City: "
read whichfield
echo -n "What would you like to change it to? "
read changeto

NPOST=$(grep $con2mod $CONTACTS | cut -d ";" -f 2-6)
PPRE=$(cut -d ";" -f 1 $CONTACTS | grep $con2mod)
PPOST=$(grep $con2mod $CONTACTS | cut -d ";" -f 3-6)
EPRE=$(cut -d ";" -f 1,2 $CONTACTS | grep $con2mod)
EPOST=$(grep $con2mod $CONTACTS | cut -d ";" -f 4-6)
APRE=$(cut -d ";" -f 1,2,3 $CONTACTS | grep $con2mod)
APOST=$(grep $con2mod $CONTACTS | cut -d ";" -f 5-6)
SPRE=$(cut -d ";" -f 1,2,3,4 $CONTACTS | grep $con2mod)
SPOST=$(grep $con2mod $CONTACTS | cut -d ";" -f 6)
CPRE=$(cut -d ";" -f 1,2,3,4,5 $CONTACTS | grep $con2mod)

if [ "$whichfield" == "n" ]
	then 
		cat $CONTACTS | grep -v $con2mod>$CONTEMP
		echo "$changeto ; $NPOST">>$CONTEMP
            	mv $CONTEMP $CONTACTS
		echo "$changeto ; $NPOST"
elif [ "$whichfield" == "p" ]
	then
		cat $CONTACTS | grep -v $con2mod>$CONTEMP
		echo "$PPRE ; $changeto ; $PPOST">>$CONTEMP                
		mv $CONTEMP $CONTACTS
		echo "$PPRE ; $changeto ; $PPOST"
elif [ "$whichfield" == "e" ]
        then 
		cat $CONTACTS | grep -v $con2mod>$CONTEMP
		echo "$EPRE ; $changeto ; $EPOST">>$CONTEMP                
                mv $CONTEMP $CONTACTS
		echo "$EPRE ; $changeto ; $EPOST"               
elif [ "$whichfield" == "a" ]
        then    
		cat $CONTACTS | grep -v $con2mod>$CONTEMP
                echo "$APRE ; $changeto ; $APOST">>$CONTEMP
                mv $CONTEMP $CONTACTS
		echo "$APRE ; $changeto ; $APOST"           
elif [ "$whichfield" == "s" ]
        then    
		cat $CONTACTS | grep -v $con2mod>$CONTEMP
                echo "$SPRE ; $changeto ; $SPOST">>$CONTEMP
                mv $CONTEMP $CONTACTS
		echo "$SPRE ; $changeto ; $SPOST"     
elif [ "$whichfield" == "c" ]
        then    
		cat $CONTACTS | grep -v $con2mod>$CONTEMP
                echo "$CPRE ; $changeto">>$CONTEMP
                mv $CONTEMP $CONTACTS
		echo "$CPRE ; $changeto"

fi
read null
        exit 0
