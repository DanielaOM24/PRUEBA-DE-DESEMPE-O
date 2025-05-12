import time
#1.Define a menu for the customer to select an option.
def show_menu():
    while True:
        print("\n------MENU------")
        print("1.Add products")
        print("2.Consult products")
        print("3.Update price")
        print("4.Delete products")
        print("5.Calculate the total value")
        print("6.Show inventary")
        print("7.Exit")
        
        option= input("\n✅ Select an option 👇:") #the user is given input.
        #The functions we create are called according to the option you choose.
        if option == "1": 
            add_products()
        elif option == "2":
            consult_products()
        elif option == "3":
            update_price()
        elif option == "4":
            delete_product()
        elif option == "5": 
            calculate_total()
        elif  option == "6":
            show_inventary()    
        elif option == "7":
            print("🫡¡Good bye!")    
            break
        else:
            print("❌  Invalid option , select  (1 a 6)")                        
#2.Restore inventory
# Create an empty dictionary to store the products
inventary  ={} # is the name of our database or dictionary
#3. Function to add products
def add_products(): #the function is defined.
    while True: 
        name= input("\nName of product:") # input= asks the user for data - .strip= removes spaces at the beginning and end
        if not name:
            print("You did not enter any products")
            continue
        else:
            if name in inventary:
                print("\n⚠️ The product is already in inventory.")
            break
    #while and try are used to determine errors due to invalid data
    while True:
        try:
            price=float(input("\n What is the price of the product:"))# convert to decimal
            if price <=0:
                print("\n❌You must enter a positive value") # print if there is an error.
                print("-"*50) # decorative text.
                continue
            else: 
                print (f"\n✅The price of your product is:$ {price}")#print this text if it is correct.
                print("-"*50)
                break
        except ValueError:
                print("\n❌Invalid price. Please try again.") #print if incorrect.
                print("-"*50)           
    while True: # This loop is opened so that if the user enters an invalid character it is returned until something correct is entered.
        try:             
            Quantity=int(input("\ncWhat is the quantity of the product:")) #convert to integer.
            if Quantity <=0:
                print("\n❌You must enter an amount") #prints if the value is less than 0.
                print("-"*50) # decorative text.
                continue
            else:
                print(f"\nThe quantity of your product is :{Quantity} units") #prints the amount entered by the user.
                print("-"*50)
                break
        except ValueError:                  
            print("\n❌Invalid amount. Please try again.")#prints an error.
            print("-"*50)
        # dictionary is inventory, create an entry where the key is the product name and the value is a tuple with the price and quantity.


    inventary[name]= (price, Quantity) 
    print(f"\nProduct {name} added succesfull") # print this text.
    answer= input("\n Do you want yo add another product? (yes/no): ").strip().lower() #user input to enter data.
    if answer=="yes":
        add_products() # the function is called for the client to add another product.
    else:
        return 
    print("-"*50) #decorative text.     
#4. Function for consult a product
def consult_products(): # the function is defined
    name= input("\n Name of the product to search for:").strip().lower()#data provided by the user.
    if name in inventary: # If you determine if the name is in inventory, do the following:
        price, quantity =inventary [name] #If the product exists, the price and available quantity are extracted from the dictionary.
        print(f"\n in the moment there are {quantity} units of {name} and price units is  ${price}")# print the text.
        answer= input("Would you like to consult another product? (yes/no): ").strip().lower()#entrada de dato al usuario
        if answer=="yes":
            consult_products()# call function.
        else:
            return
        print("-"*50)#decorative text.
    else:
        print("\nthe product not is stock")#print text.
#5.Update price
def update_price(): #define funcion
    name=input("\nName of product:").strip().lower()#data input to the user.
    if name in inventary: 
        try:
            new_price=float(input("\n what is the new price of your product?:")) #enter new data to the user.
            if new_price>=0: 
                _, quantity = inventary[name] #In this case the price is ignored in order to assign a different price to the variable.
                inventary[name] = (new_price, quantity) #makes the variable exchange.
                print("\nupdating...")
                time.sleep(1.5)  # Short break for better user experience.
                print(f"✅ The price of '{name}' has been updated.") #Confirms to the user that they have been updated.
                print(f" now the price of {name} es ${new_price}")# print the entered value.
                print("-" * 50)#decorative text.
            else:
                print("\n❌ The entered value is invalid. The price cannot be negative.") #When the user makes a mistake, it notifies them
                print("-" * 50)#decorative text.
        except ValueError:
            print("\n❌ Enter numeric values ​​only.")#tells the user if they enter the data incorrectly.
            print("-" * 50)#decorative text.
    else:
        print("\n❌ Product not found.")#indicates if the product is not found.
               
        
#6.Delete a product.
def delete_product(): #the funtion is defined.
    name=input("\nName of the product you want to delete:").strip().lower() ##user data entry.
    if name in inventary: 
        del inventary[name] #from the dictionary delete inventory name or the product that was saved.
        print(f"\n🗑️ The product {name} has been elimiremoved.") # confirms that it has been deleted.
    else:
        print("\n❌ Product not found") 
#7.Calculate  total value  with lambda.
def calculate_total():
    total=sum(map(lambda item: item[0]*item[1],inventary.values())) # CCalculates the total inventory value by adding (price × quantity) of each product.# It goes through all the inventory values ​​and multiplies each price by its quantity.
    print(f"\nThe total value is:${total}") #print the total value.
#8.show all registered products.
def show_inventary(): # the function is defined.
        if not inventary: 
            print("\n📦 The inventary is empty.")# shows if inventory is empty.
            return
        print("\n📋 complete inventary:")
        print("-" * 50)
        for name, (price, quantity) in inventary.items(): # If it's not empty, display each product with price and quantity.
            print(f"🛒 Product: {name}")#prints the product.
            print(f"   price: ${price}")#print price.
            print(f"   quantity: {quantity} units")# print quantity
            print("-" * 50)#decorative text.
        time.sleep(3)
show_menu()

        
    
        
        
        
        
        
                        
            
                

        
      
            
            


        
    
    
    
   
    


    
    
