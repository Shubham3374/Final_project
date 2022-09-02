from unicodedata import name


class Store:
    def __init__(self,name):

        self.store_name = name
        self.food = {}
        self.food_id = 0
        self.user_id = 0
        self.user_details = {}
        self.ordered_item = []
        self.update_details = {}

    def addfood(self):
        try:
            name = input("Enter the name of food : ")
            quantity = int(input("Enter the quantity which you want :"))
            price = float(input("Enter the price of that food item :"))
            stock = float(input("Enter the available stock :"))
            discount = float(input ("Enter available discount on that item : "))
            food_item = {"Name":name , "Quantity":quantity , "Price":price , "Stock":stock , "Discount":discount}
            self.food_id = len(self.food) + 1
            self.food[self.food_id] = food_item
        

            print("Food item added successfully .")

        except Exception :
            print("Something went wrong .Please try again .")

    def editfood(self):
        id = int(input("Enter the food id :"))
        if id in self.food:
            self.food[id]["Name"] = input("Enter the food item you want to update :")
            print("Updated successfully .")
        else :
            ("Invalid keys .") 

    def viewfood(self):
        if len(self.food)!= 0:
            for i in self.food:
                print(f"Fruit Id {i}")
                for j in self.food[i]:
                    print(j, ":", self.food[i][j])
                print()
        else:
            print("Sorry No Food item")

    def removefood(self):
        id = int(input("Enter the food id :"))

        if id in self.food:
            self.food.pop(id)
            print("Item of that id removed successfully .")
        else:
            print("Invalid Id or not available item .")

    def user_reg(self):
        try:
            name = input("Enter your name : ")
            mobnum = int(input("Enter your number :"))
            email = input("Enter your email: ")
            address = input("Enter your address : ")
            pswrd = input("enter your password :")
            new_user = {"Name": name,"Mobile number":mobnum,"Email":email,"Address":address,"Password":pswrd}
            self.user_id = len(self.user_details) + 1
            self.user_details[self.user_id] = new_user
            print("User registered successfully .", self.user_details)

        except Exception :
            print("Something went wrong . Please re enter details .")

    def user_login(self):
        name = input("Enter your name : ")
        pswrd = input("enter your password :")
        if name or pswrd in self.user_details:
            print("User logged in successfully .")

        else:
            print("Invalid username and password. ")

    def update_profile(self):
        print("What you want to update :")
        print("1 . Name :")
        print("2 . Password :")
        print("3 . Mobile number :")
        print("4 . Email :")
        print("5 . Address :")

    
        try:
            name = input("Enter your updated name : ")
            mobnum = int(input("Enter your updated number :"))
            email = input("Enter your updated email: ")
            address = input("Enter your updated address : ")
            pswrd = input("enter your updated password :")
            new_details = {"Name": name,"Mobile number":mobnum,"Email":email,"Address":address,"Password":pswrd}
            self.user_id = len(self.update_details) + 1
            self.update_details[self.user_id] = new_details
            print("User previous details .", self.user_details)
            print("User updated details  .", self.update_details)


        except Exception :
            print("Something went wrong . Please re enter details .")

            
                       

    
    def place_order(self):
        print("The list item shown as follows:")
        print("1 . Tandoori Chicken .")
        print("2 . Vegan Burger .")
        print("3 . Truffle Cake .")

        option = int(input("Enter option of item you want to order :"))
        
        if option == 1:
            name = (input("Enter the name of food :"))
            quantity = int(input("Enter the quantity :"))
            price = int(input("Enter the price of that item :"))
            new_order = [name , quantity , price]
            self.ordered_item.append(new_order)
            print(f"Tandoori chicken of INR Rs {price} of {quantity} placed successfully")

        elif option == 2:
            name = (input("Enter the name of food :"))
            quantity = int(input("Enter the quantity :"))
            price = int(input("Enter the price of that item :"))
            new_order = [name , quantity , price]
            self.ordered_item.append(new_order)
            print(f"Vegan Burger of INR Rs {price} of {quantity} placed successfully")

        elif option == 3:
            name = (input("Enter the name of food :"))
            quantity = int(input("Enter the quantity :"))
            price = int(input("Enter the price of that item :"))
            new_order = [name , quantity , price]
            self.ordered_item.append(new_order)
            print(f"Truffle Cake of INR Rs {price} of {quantity} placed successfully")

        else :
            exit

    def order_history(self):
        print(f"Order history of previous one is {self.ordered_item}")






if __name__ == '__main__':
    s = Store("Zomato")

while True :
    print(f"Welcome to our Food Ordering App {s.store_name}.")

    print("1 . Admin")
    print("2 . User ")
    print("3 . Exit ")

    option = int(input("Enter your option for further process : "))
    if option == 1 :
        print("1 .Add food")
        print("2 .Edit food")
        print("3 .View food")
        print("4 .Remove Food")
        key = int(input(""))
        if key == 1 :
            s.addfood()

        elif key == 2 :
            s.editfood()

        elif key == 3:
            s.viewfood()

        elif key == 4:
            s.removefood()

        else:
            exit
    elif option == 2 :
        print("1. Register .")
        print("2. Log in .")
        print("3. User ")
        key = int(input("Enter the option which you want : "))
        if key == 1 :
            s.user_reg()
        
        elif key == 2 :
            s.user_login()

        elif key == 3:
            print("1.Place new order .")
            print("2.Order History .")
            print("3.Update Profile . ")

            x = int(input("Enter the option :"))

            
            if x == 1 :
                s.place_order()
                
            elif x == 2 :
                s.order_history()
                
            elif x == 3 :
                s.update_profile()

            



        else:
            exit
            





       