import json 

class admin:
    
    def __init__(self):
        self.food={}
        self.food_id = len(self.food)+1

    def add_food_item(self):
        self.name=input("enter the name of the food item : ")
        self.quantity=int(input("enter the quantity of the food item : "))
        self.price=int(input("enter the price of the food item : "))
        self.stock=int(input("enter the stock of the food item : "))
        self.discount=int(input("enter the discount of the food item : "))
        self.item={"name":self.name, "quantity":self.quantity, "price":self.price, "stock":self.stock, "discount":self.discount}
        #print(self.item)
        self.food_id = len(self.food)+1
        self.food[self.food_id]=self.item
        #print(self.food)
        with open ("food_item.json","w") as f:
            json.dump(self.food,f)
        print("Item added successfully......")    

    def remove_food(self):
        for k,v in self.food.items():
            print("food id",k,"and food item",v) 
        del self.food[int(input("enter the food id which you wanted to delete : "))]
        with open ("food_item.json","w") as f:
            json.dump(self.food,f)
        print("Item deleted successfully......") 

    def view_food_item(self):
        for k,v in self.food.items():
            print("food id",k,"and food item",v)

    def edit_food_item(self):
        food_id = int(input("enter which food id you want to edit : "))
        for i in self.food[food_id]:
            self.food[food_id][i] = input(f"enter the {i} you want to update : ")
        with open("food_item.json","w") as f:
            json.dump(self.food,f)
        print("food details have been updated.....")    

                

'''x=admin()
x.add_food_item() 
x.add_food_item()
x.remove_food()
x.view_food_item()
x.add_food_item()
x.edit_food_item()'''