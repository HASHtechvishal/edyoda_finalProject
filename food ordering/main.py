from admin import *
from user import *
import sys

print (".............................Welcome to the FOOD ordring app.....................") 

print("========================Please select your roll for food ordring app================") 
role = int(input(" \n1. Admin\n2. User\n3. Exit\n\nEnter your input here -- ")) 

if role==1:
        res=admin()
        while True:
            print("enter 1 for add food item...")
            print("enter 2 for Edit food item...")
            print("enter 3 for remove food item...")
            print("enter 4 for view food item...")
            print("enter 0 for Exit")
            admin_input = int(input("enter your preference.."))
            if admin_input==1:
                res.add_food_item()
            elif admin_input==2:
                res.edit_food_item()
            elif admin_input==3:
                res.remove_food()
            elif admin_input==4:
                res.view_food_item()
            elif admin_input==0:
                sys.exit()
            else:
                print("please enter valid input....")

elif role==2:
        res=user()
        print("...............enter Y/N for yes/no..................")
        register = input("already register? : ").upper()
        if register == "Y":
             res.login()
        elif register == "N":
             print("..........please register yourself........")
             res.register()
             print("..........welcome user please login for place your order........")
             res.login()
        else:
             print("please enter Y/N only, lets try again........")
elif role==3:
     print (".............................Thank You,please visit again.....................")
     sys.exit()
else:
     print("Please enter only given inputs")                            
