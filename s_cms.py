#--------------------------bll------------------------------------------------------------------------
listid=[]
listname=[]
listadd=[]
listmob=[]

def addcus(id,name,add,mob):
    listid.append(id)
    listname.append(name)
    listadd.append(add)
    listmob.append(mob)

def searchcus(id):
    if listid.__contains__(id):
        i=listid.index(id)
        print("customer id: ",listid[i],"customer name: ",listname[i],"customer address: " \
              ,listadd[i],"customer mob: ",listmob[i])

    else:
        print("id not found")

def deletecus(id):
    if listid.__contains__(id):
        i=listid.index(id)
        listid.pop(i)
        listname.pop(i)
        listadd.pop(i)
        listmob.pop(i)


def modifycus(id,name,add,mob):
    if listid.__contains__(id):
        i=listid.index(id)
        listname[i]=name
        listadd[i]=add
        listmob[i]=mob




#pl-----------------------------------------------------------------------------------------------

while True:
    print("1.add customer\n2.search customer\n3.delete customer\n4.modify customer")
    ch = input("enter your choice")
    if ch=="1":
        id=int(input("enter customer id"))
        name=input("enter customer name")
        add=input("enter customer address")
        mob=input("enter customer moile no")
        addcus(id, name, add, mob)
        print("customer added successfully")

    elif ch=="2":
        id=int(input("enter id of customer to be searched"))
        searchcus(id)

    elif ch=="3":
        id=int(input("enter customer id"))
        deletecus(id)
        print("customer deleted")

    elif ch=="4":
        id=int(input("enter customer id to be modified"))
        name=input("enter name")
        add=input("enter address")
        mob=input("enter mob no")
        modifycus(id, name, add, mob)

    else:
        break
