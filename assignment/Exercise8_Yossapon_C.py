print("--welcome to secret shop--")
ID = input("ID :")
Password = input("Password :")
if ID != "anonymous01" or Password != "123456":
    print("Sorry your ID or Password not correct")
elif ID == "anonymous01" and Password == "123456":
    print(f"Welcome {ID}")
    print("========================\n MENU")
    ############################# รายการสินค้า
    print("1.Cocacola 19THB\n2.Pringles 40THB\n3.Euro Cake 5THB")
    Menu_select = input("Whant do you whant to buy (select number1 ,2 ,3): ")
    item_select = int(input("How many pieces do you need?: "))
    if Menu_select == "1":
        total = item_select * 19
        print("Total",total,"THB")
    elif Menu_select == "2":
        total = item_select * 40
        print("Total", total, "THB")
    elif Menu_select == "3":
        total = item_select * 5
        print("Total", total, "THB")
    else:
        print("YOU PICK A WRONG NUMBER!")