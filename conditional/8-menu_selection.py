# menu selection add , update , delete or show
menu = input("Enter Menu Option(add,update,delete,show):").lower()

if menu == "add":
    print("Add Operation")
elif menu == "update":
    print("Update Operation")
elif menu == "delete":
    print("Delete Operation")
elif menu == "show":
    print("Show Operation")
else:
    print("Invalid Menu Option")
