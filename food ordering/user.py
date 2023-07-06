import json
import sys

class user:

      def __init__(self):
            self.user = {}
            self.user_id = len(self.user)+1

      def register(self):
                
            with open ("user_info.json") as json_file:
                       data = json.load(json_file)

            if data != None:
                             
                        with open("user_info.json", "r") as file:
                           data = json.load(file)
                             
                           self.name = input("Enter your name : ")
                           self.number = int(input("Enter your phone number : "))
                           self.email = input("Enter your email address : ")
                           self.address = input("Enter your address : ")
                           self.password = input("Enter your password : ")
                           self.userINFO = {"name":self.name,"number":self.number,"email":self.email,"address":self.address,"password":self.password}
                             #print(self.userINFO)
                           self.user_id = len(data)+1
                           self.user[self.user_id]=self.userINFO
                             
                           data.update(self.user)

                           with open("user_info.json", "w") as file:
                                 json.dump(data, file,indent=4)
                                 print("Welcome",self.name,", Your Register Now......")

            else:
                       
                             self.name = input("Enter your name : ")
                             self.number = int(input("Enter your phone number : "))
                             self.email = input("Enter your email address : ")
                             self.address = input("Enter your address : ")
                             self.password = input("Enter your password : ")
                             self.userINFO={"name":self.name,"number":self.number,"email":self.email,"address":self.address,"password":self.password}

                             self.user_id = len(self.user)+1
                             self.user[self.user_id]=self.userINFO

                             with open ("user_info.json","w") as f:
                               json.dump(self.user,f,indent=4)
                               print("User added successfully......")


      def login(self):
                
            with open ("user_info.json", "r") as json_file:
                  data = json.load(json_file)
            user_name = input("Enter you name : ")
            user_pass = input("Enter your password : ")

            for key,value in data.items():
                  if (user_name == value['name']) and (user_pass == value['password']):
                       global user_key
                       user_key = key
                       print(".............welcome ",value['name'],"Your user id is (",key,")................")
                       print(".............Please Select your option........")
                       print("FOR\n1. New Order Enter - N\n2. Update Profile Enter - P (user id (",key,"))\n3. Order History Enter - H\n4.Cancel process enter - C")
                       option = input("Enter your option here : ").upper()
                       
                       if option == "N":
                             print("..............Enter the valide input for new order................")
                             x.new_order()
                       elif option == "P":
                             print("..............Enter the valide input for update your profile................")
                             x.update_info()
                       elif option == "C":
                             sys.exit()
                       elif option == "H":
                            x.order_history()
                       else:
                             print("Please enter valid option..lets login again")
                             x.login()
                             sys.exit()
                             
            else:
                       print("incorrect name or password, please try again...")
                       print("FOR\n1. New Register Enter - 1\n2. Try again Enter - 2")
                       retry = int(input("Enter Your option : "))
                       if retry == 1:
                             x.register()
                       elif retry == 2:
                            x.login()
                       else:
                             print("Please enter vaild input....")
                             sys.exit()


      def new_order(self):
              
              with open ("food_item.json") as json_file:
                       data = json.load(json_file)
                       print("FOR")
                       for k,v in data.items():
                         print(v['name']+" Enter - "+k)
              new_order = int(input("Enter your input for new order : "))
              print("=====================================================================================================================")
 #########################################################################################################################################              
              if new_order == 1:
                    print("...............Your order is Tandoori Chicken, Please select your order details also.........")
                    for v in data:
                          '''print(data[str(new_order)]['quantity'])
                          print(data[str(new_order)]['price'])
                          print(data[str(new_order)]['discount'])'''

                    print("Quantity -",data[str(new_order)]['quantity'],"Qty\t\t\tPrice -",data[str(new_order)]['price'],"INR\t\t\tDiscount -",data[str(new_order)]['discount'],"%")

                    qty = int(input("Enter your food quantity : "))
                    print("=====================================================================================================================") 

                    if data[str(new_order)]['quantity'] < qty:
                          print("out of quantity")
                    else:
                         remain_qty = data[str(new_order)]['quantity'] - qty
                         total_price = data[str(new_order)]['price'] * qty
                         discount =  total_price - (total_price * data[str(new_order)]['discount'] / 100)

                         print(f"............Your order...........\n",data[str(new_order)]['name'],"\n Quantity -",qty,"\t\t\tTotal price -",total_price,"INR\t\t\tDiscounted price -",discount,"INR")
                         print("=====================================================================================================================")
                         print("confirm order Enter -- C")

                         inp = input("Enter your input for Confirm or Add order : ").upper()
                         print("=====================================================================================================================")


                         if inp == "C":
                                
                              with open("user_orders.json", "r") as file:
                                 data_con = json.load(file)
                              user_order = {"order name":data[str(new_order)]['name'],"quantity":qty,"total price":total_price,"discounted price":discount}
                              self.user_id = user_key
                              self.user[self.user_id]=user_order
                              data_con.update(self.user)
                              with open ("user_orders.json","w") as f:
                                json.dump(data_con,f,indent=4)
                                print("Item added successfully......")


                                print("...................Your order is confirm, Please proceed for the payment...................")
                                print("Please pay your payment by Enter - P\t\t\t\t\tcancel your order Enter -C")
                                pay = input("Enter your payment input : ").upper()
                                print("=====================================================================================================================")

                              if pay == "P":
                                     
                                     #print(remain_qty)
                                     data[str(new_order)]['quantity'] = remain_qty
                                     with open("food_item.json","w") as f:
                                       json.dump(data,f,indent=4)
                  
                                     print(".............Payment done-------Thanks for ordering......")
                                     sys.exit()
                              elif pay == "C":
                                     print("..........Your order is cancel......Thanks for using the app.............")
                                     del data_con[str(user_key)]
                                     with open ("user_orders.json","w") as f:
                                      json.dump(data_con,f,indent=4)
                                     sys.exit()
                              else:
                                     print("Please enter your valid input")
                  
                         else:
                               print("Please enter valid input")

########################################################################################################################################################
              elif new_order == 2:
                    print("...............Your order is Vegan Burger,Please select your order details also.........")
                    for v in data:
                          '''print(data[str(new_order)]['quantity'])
                          print(data[str(new_order)]['price'])
                          print(data[str(new_order)]['discount'])'''

                    print("Quantity -",data[str(new_order)]['quantity'],"Qty\t\t\tPrice -",data[str(new_order)]['price'],"INR\t\t\tDiscount -",data[str(new_order)]['discount'],"%")
                    
                    qty = int(input("Enter your food quantity : "))

                    if data[str(new_order)]['quantity'] < qty:
                          print("out of quantity")
                    else:
                         remain_qty = data[str(new_order)]['quantity'] - qty
                         total_price = data[str(new_order)]['price'] * qty
                         discount =  total_price - (total_price * data[str(new_order)]['discount'] / 100)

                         print(f"............Your order...........\n",data[str(new_order)]['name'],"\n Quantity -",qty,"\t\t\tTotal price -",total_price,"INR\t\t\tDiscounted price -",discount,"INR")
                         print("=====================================================================================================================")
                         print("confirm order Enter -- C")

                         inp = input("Enter your input for Confirm or Add order : ").upper()
                         print("=====================================================================================================================")

                         if inp == "C":
                               
                              with open("user_orders.json", "r") as file:
                                 data_con = json.load(file)
                              user_order = {"order name":data[str(new_order)]['name'],"quantity":qty,"total price":total_price,"discounted price":discount}
                              self.user_id = user_key
                              self.user[self.user_id]=user_order
                              data_con.update(self.user)
                              with open ("user_orders.json","w") as f:
                                json.dump(data_con,f,indent=4)
                                print("Item added successfully......")


                                print("...................Your order is confirm, Please proceed for the payment...................")
                                print("Please pay your payment by Enter - P\t\t\t\t\tcancel your order Enter -C")
                                pay = input("Enter your payment input : ").upper()
                                print("=====================================================================================================================")

                              if pay == "P":
                                     
                                     #print(remain_qty)
                                     data[str(new_order)]['quantity'] = remain_qty
                                     with open("food_item.json","w") as f:
                                       json.dump(data,f,indent=4)                                     

                                     print(".............Payment done-------Thanks for ordering......")
                                     sys.exit()
                              elif pay == "C":
                                     print("..........Your order is cancel......Thanks for using the app.............")
                                     del data_con[str(user_key)]
                                     with open ("user_orders.json","w") as f:
                                      json.dump(data_con,f,indent=4)
                                     sys.exit()
                              else:
                                     print("Please enter your valid input")

                         
 ###########################################################################################################################################################                        
              elif new_order == 3:
                    print("...............Your order is Truffle Cake,Please select your order details also.........")
                    for v in data:
                          '''print(data[str(new_order)]['quantity'])
                          print(data[str(new_order)]['price'])
                          print(data[str(new_order)]['discount'])'''

                    print("Quantity -",data[str(new_order)]['quantity'],"Qty\t\t\tPrice -",data[str(new_order)]['price'],"INR\t\t\tDiscount -",data[str(new_order)]['discount'],"%") 
                    
                    qty = int(input("Enter your food quantity : "))

                    if data[str(new_order)]['quantity'] < qty:
                          print("out of quantity")

                    else:
                         remain_qty = data[str(new_order)]['quantity'] - qty
                         total_price = data[str(new_order)]['price'] * qty
                         discount =  total_price - (total_price * data[str(new_order)]['discount'] / 100)

                         print(f"............Your order...........\n",data[str(new_order)]['name'],"\n Quantity -",qty,"\t\t\tTotal price -",total_price,"INR\t\t\tDiscounted price -",discount,"INR")

                         print("=====================================================================================================================")
                         print("confirm order Enter -- C")

                         inp = input("Enter your input for Confirm or Add order : ").upper()
                         print("=====================================================================================================================")

                         if inp == "C":
                               
                              with open("user_orders.json", "r") as file:
                                 data_con = json.load(file)
                              user_order = {"order name":data[str(new_order)]['name'],"quantity":qty,"total price":total_price,"discounted price":discount}
                              self.user_id = user_key
                              self.user[self.user_id]=user_order
                              data_con.update(self.user)
                              with open ("user_orders.json","w") as f:
                                json.dump(data_con,f,indent=4)
                                print("Item added successfully......")


                                print("...................Your order is confirm, Please proceed for the payment...................")
                                print("Please pay your payment by Enter - P\t\t\t\t\tcancel your order Enter -C")
                                pay = input("Enter your payment input : ").upper()
                                print("=====================================================================================================================")

                              if pay == "P":
                                     
                                     #print(remain_qty)
                                     data[str(new_order)]['quantity'] = remain_qty
                                     with open("food_item.json","w") as f:
                                       json.dump(data,f,indent=4)
                                     
                                     print(".............Payment done-------Thanks for ordering......")
                                     sys.exit()
                                     
                              elif pay == "C":
                                     print("..........Your order is cancel......Thanks for using the app.............")
                                     del data_con[str(user_key)]
                                     with open ("user_orders.json","w") as f:
                                      json.dump(data_con,f,indent=4)
                                     sys.exit()
                              else:
                                     print("Please enter your valid input")
      
              else:
                    print("please enter valide input")


      def order_history(self):
            with open("user_info.json","r") as f:
                  data = json.load(f)
                  print("=====================================================================================================================")
                  print("...........Hey,",data[str(user_key)]['name'],"Your Order History is --------------------------")
                  with open("user_orders.json", "r") as file:
                        data_his = json.load(file)
                        print("1.Your Order is - ",data_his[str(user_key)]['order name'],"\n2.Total Payment - ",data_his[str(user_key)]['discounted price'],"\n3.Order Quantity - ",data_his[str(user_key)]['quantity'])
                        exit()
                              



      def update_info(self):
             
             user_id = input("Enter your user id here : ")

             with open ("user_info.json") as json_file:
                data = json.load(json_file)
                
                for i in data[user_id]:
                      data[user_id][i] = input(f"Enter the {i} you want to update : ")

                with open("user_info.json","w") as f:
                      json.dump(data,f,indent=4)
                      print("user details have been updated....") 
                      exit()
                       

       

x=user()
#x.register()
#x.login()
#x.new_order()
#x.update_info()
