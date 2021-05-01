
contactlist = []

name = input("Contact name:")
phone = input("Phone #:")
email = input("Email address:")
addr = input("Street address:")
sub = input("Suburb:")
city = input("City:")
print("Are you sure you want to add this contact?")

savecontact = input("y/n ")
if savecontact == "y":
    print("Contact "+name+" saved.")
    contact = []+[name]+[phone]+[email]+[addr]+[sub]+[city]
    contactlist.append(contact)
else:
    print("Contact "+name+" not saved.")
