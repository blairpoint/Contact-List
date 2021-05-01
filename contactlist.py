import sys
class Contact:
    def __str__(self):
        return "Name: "+self.name+" Email: "+self.email+" Phone: "+self.phone

    def convert_data(self):
        return self.name +";"+self.phone+";"+ self.email+";"+self.addr+";"+self.sub+";"+self.city

    def convert_data_display(self):
        return "\nName: "+self.name +"\n"+"Phone: "+self.phone+"\n"+"Email: "+ self.email+"\n"+"Address: "+self.addr+"\n"+"Suburb: "+self.sub+"\n"+"City: "+self.city+"\n"


    def __init__(self,name,phone,email,addr,sub,city):
        self.name = name
        self.phone = phone
        self.email = email
        self.addr = addr
        self.sub = sub
        self.city = city

contactlist = []

with open('contacts.txt') as fp:
    for line in fp.readlines():
        if line.strip():
            d = line.split(";")
            contactlist.append(Contact(d[0], d[1], d[2], d[3], d[4], d[5]))

def add():
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
        contactlist.append(Contact(name, phone, email, addr, sub, city))
    else:
        print("Contact "+name+" not saved.")
    save()

def list():
    for list in contactlist:
        print(list)

def search():
    tosearch = input("Name to search: ")
    for c in contactlist:

        if tosearch.lower() == c.name.lower():
            print(c.convert_data_display())



def save():
    with open('contacts.txt', 'w') as fp:
        print("Saving changes")
        for it in contactlist:
            fp.write(it.convert_data()+"\n")



def delete():
    todel = input("which contact would you like do delete? ")
    flag = True
    for c in contactlist:
        if todel.lower().rstrip() == c.name.lower().rstrip():
            print("Are you sure you want to delete contact "+todel+" ?")
            delcontact = input("y/n ")
            if delcontact == "y":
                print("Contact " + todel + " deleted.")
                contactlist.remove(c)
            else:
                print("Contact " + todel + " not deleted.")
            save()
            flag = False
    if flag == True:
        print("not found.")

def modify():
    tomod = input("which contact would you like do modify? ")
    flag = True
    for c in contactlist:
        print('.'+c.name.lower().rstrip()+'.'+tomod.lower().rstrip()+'.')
        if tomod.lower().rstrip() == c.name.lower().rstrip():

            print("[n] Name: "+c.name)
            print("[p] Phone: "+c.phone)
            print("[e] Email address: "+c.email)
            print("[a] Street Address: "+c.addr)
            print("[s] Suburb: "+c.sub)
            print("[c] City: "+c.city)

            fieldmod = input("Which field do you want to change? ")
            changeto = input("Enter new value for field ")

            print("Save changes to contact "+tomod+" ?")
            delcontact = input("y/n ")
            if delcontact == "y":
                if fieldmod == "n":
                    c.name = changeto
                elif fieldmod == "p":
                    c.phone = changeto
                elif fieldmod == "e":
                    c.email = changeto
                elif fieldmod == "a":
                    c.addr = changeto
                elif fieldmod == "s":
                    c.sub = changeto
                elif fieldmod == "c":
                    c.city = changeto
                print("Contact " + tomod + " updated.")
                save()
            else:
                print("Contact " + tomod + " not updated.")
            save()
            flag = False
    if flag == True:
        print("not found.")




def menu():
    print("Contact List")
    print("Enter selection: ")
    print("[a] add")
    print("[l] list")
    print("[s] search")
    print("[m] modify")
    print("[d] delete")
    print("[x] exit")
    menu = input()

    if menu == "a":
        add()
    elif menu == "l":
        list()
    elif menu == "s":
        search()
    elif menu == "m":
        modify()
    elif menu == "d":
        delete()
    elif menu == "x":
        sys.exit()
while True:
    menu()
