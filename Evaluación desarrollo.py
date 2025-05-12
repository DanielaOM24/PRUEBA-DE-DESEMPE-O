import time
#store inventary
#1.Add products
def show_menu(): #Define a menu for the customer to select an option.
    while True:
        print("\n-------Menu-------")
        print ("1.Add products:")
        print ("2.Consult products:")
        print ("3.Update price:")
        print("4.Calculate total value:")
        print("5.Show inventary:")
        print("6.Delete product:")
        print("7.Exit.")
        option= input("Select an option:").strip()#the user is given input.
        if option == ("1"):
            add_product()
        elif option == ("2"):
            consult_products()    
        elif option == ("3"):
            update_price ()
        elif option == ("4"):
            calculate_total()
        elif option == ("5"):
            delete_product()  
        elif option == ("6"):
            show_inventary() 
        elif option == ("7"):
            print("GoodbySee you soon, thank you for using our service.")  
            break
        else:
            print("Invalid option. Select (1 to 6)")
#2.We create an empty dictionary to store the products.
inventary={} #it is the name of our database.
#3:function to add products.
def add_product(): #the function is defined.
    while True:
        name=input("\nName of the product:").strip().lower() # input = prompts the user for input - . strip = removes spaces at the beginning and end
        if not name:
            print("You did not enter any product.")
            continue
        if name in inventary:
            print("\n⚠️ The product is already in inventory.")
            break   
#used while and try to determine errors due to invalid data.
    while True:
        try:
            price= float(input("\n What is the price of the product:")) #converts the text to decimal.
            if price <=0:
                print("\n❌you must enter a positive value") #show this if there is an error.
                print("-"*45) # decorative text.
                continue
            else:
                print(f"\n✅The price of your product is :$ {price}")#prints the data entered.
                print("-"*45)#decorative text.
                break
        except ValueError:
                print("\n❌Invalid price.Try again.")    
                print("-"*45) #decorative text.
    while True: ## This loop is opened so that if the user enters an invalid character, it is returned until the user enters something correct.
        try:
            quantity=float (input("\nwhat is the quantity of the product:"))
            if quantity <=0:
                print("\n❌ You must enter an amount")#print if the value is less than 0.
                print("-"*45) #decorative text.
                continue
            else:
                print("The quantity  of your productos is:{quantity} units.")
                print("-"*45) #decorative text.
                break
        except ValueError:
            print("\n❌invalid quantity. Try again.")  
            print("-"*45)# decorative text.
    inventary=[name]=(price,quantity)## dictionary is inventory, create an entry where the key is the product name and the value is a tuple with the price and quantity.
    print(f"\n✅The Product {name} added succesfull.")
    while True:
        Answer=input("\n Do you want to add another product? (yes/no)").strip().lower()
        if Answer== "yes":
            add_product() #The function is called so that the client can add another product.
        else:
            return
        print("-"*45)
#4.consult products
def consult_products(): #the function is defined.
    name= input("\n name of the product to search for:").strip().lower()
    if name in inventary:#If you determine if the name is in inventory, do the following:
        price,quantity=inventary[name]
        print(f"In this moment there are {quantity} and the value of the unit is {price}")
        Answer=input("\n Do you want to consult another product? (yes/no)").strip().lower()
        if Answer== "yes":
            consult_products() 
        else:    
            return
        print("-"*45) #decorative text.
    else:
        print("\n The product is not in stock.") #print text.
 #5.Update price.     
def update_price():  #the function is defined.
    name= input("\n Name of the product you want to update:").strip().lower() #user input.
    if name in inventary: 
        try:
            new_price=float(input("\n What is the new price of your product?:")) #user input.
            if new_price>=0:
                _,quantity=inventary[name] #In this case the price is ignored in order to assign a different price to the variable.
                inventary[name] =(new_price,quantity)
                print("\n Actualizando...")
                time.sleep(2) # Short pause for better user experience
                print(f"✅Thehe price of {name} has been updated.")#confirms to the user that the data was.
                print(f"\n The new price of your prudct is: ${new_price}")
                print("-"*45)
            else:
                print("❌The entered value is invalid. The price cannot be negative.") #When the user makes a mistake, it notifies them.
                print("-" * 50)#decorative text.
        except ValueError:
                print("\n❌ Enter numeric values ​​only.")#tells the user if they enter the data incorrectly.
    else: 
        print("\n❌Product no found.")#indicates that the product is not.
#6.delete products
def delete_product(): #The function is defined.
    name= input("\nName of product you want tyo delete:").strip().lower()#user input.
    if name in inventary:
        del inventary[name] # del is used to delete name from the dictionary.
        print (f"\n🗑️ The product {name} has been removed.") #confirms that we deleted a product.
    else:
        print("\n❌Product not found")
 #7.calculate value total with lambda.
def calculate_total():
     total=sum (map(lambda item: item[0]*item[1],inventary.values()))#Calculate the total inventory value by adding (price × quantity) of each product.# Loop through all inventory values ​​and multiply each price by its quantity.       
     print(f"The total value of the inventary is : $ {total}")#imprime el valor total.
#8.show all inventary.
def show_inventary():# the function is defined.
    if not inventary:
        print(f"\n📦 The inventary is empty.") #If the user does not enter anything, it shows that it is empty.
        return
    print("\n 📋Complete inventary:")
    print("-"*45)
    for name,(price,quantity) in inventary.items():#If not empty, show each product with price and quantity.
        print(f"🛒 Product: {name}") #print the product  entered by the user.
        print(f"   Price: ${price}") #print price.
        print(f"   quantity: {quantity} units") #print quantity.
        print("-" * 50)#decorative text 
        time.sleep(3)
show_menu()    
     

   
            
    
        
        
    
    
    
                
                


                
                
            
    
     
          
        
            
        
        
    
    
    
         
        
        
            
    


       
              

                
                
                
                
                
                
                
                
                
                
                
            
    
    
    
            
            