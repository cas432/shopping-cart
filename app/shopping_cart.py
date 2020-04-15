
import pytest
from dotenv import load_dotenv
import os
from datetime import datetime

 
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price_per": "N"},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99, "price_per": "N"},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49, "price_per": "N"},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price_per": "N"},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99, "price_per": "N"},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99, "price_per": "N"},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50, "price_per": "N"},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25, "price_per": "N"},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50, "price_per": "N"},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99, "price_per": "N"},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99, "price_per": "N"},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50, "price_per": "N"},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00, "price_per": "N"},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99, "price_per": "N"},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50, "price_per": "N"},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50, "price_per": "N"},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99, "price_per": "N"},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50, "price_per": "N"},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99, "price_per": "N"},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25, "price_per": "N"},
    {"id":21, "name": "Organic Bananas", "department": "fruit", "aisle": "produce", "price": 0.79, "price_per": "Y"},
    {"id":22, "name": "Organic Apples", "department": "fruit", "aisle": "produce", "price": 1.20, "price_per": "Y"}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017



def to_usd(my_price):
    '''Convert numeric value into currency formatting'''
    return f"${my_price:,.2f}"

def filename_timestamp():
    '''Convert timestamp into format for file name'''
    return datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")

def readable_timestamp():
    '''Convert timestamp info into readable form for user receipt'''
    return datetime.now().strftime("%Y-%m-%d %I:%M %p")

def find_product():
    '''Find the proper product'''
    selected_ids.append(selected_id)
    int_selected_id = int(selected_id) 
    return int

def find_id_name(my_id):
    return my_id["name"]

def print_message(message):
    print(divider)
    print(message)
    print(divider)
    


if __name__ == "__main__":
    #PART I: CAPTURE USER INPUT

    #Initialize Variables/Lists

    selected_ids = []
    all_ids = []
    lbs = []
    total_price = 0
    x = 0 #lbs index number 
    divider = "-------------------------"
    receipt = ""

    print_message("WELCOME!")

    #Create list of all valid IDs
    for p in products:
        Id_num =str(p["id"])
        all_ids.append(Id_num)

    #Enter and Validate Inputs   
    while True: 
        selected_id = input("Please input a product ID (Typye 'DONE' when finished): ")
                    
    
        if selected_id in all_ids:
            selected_ids.append(selected_id)
            int_selected_id = int(selected_id) 
            int_selected_id_minus_1 = int_selected_id - 1 # -1 because index starts at 0
                    
            if products[int_selected_id_minus_1].get("price_per") == "Y":
                pounds = input("    How many pounds would you would like to purchase?: ")
                float_pounds = float(pounds)
                lbs.append(float_pounds)
            
                
        elif selected_id == "DONE":
            break

        else:
            print("\n    ID not found. Please enter a valid ID or type 'DONE' to finish shopping.\n")
            

    # PART II: DISPLAY OUTPUT

   

    #file_path = os.path.join(os.path.dirname(__file__), "receipts", today_file_name + ".txt")
    file_path = "receipts/" + filename_timestamp() + ".txt"

    


    #Print out Receipt/Write File
    with open(file_path, "w") as file:

        receipt += divider
        receipt += "\nGREEN FOODS GROCERY\n"
        receipt += "(123)-555-1234\n"
        receipt +="WWW.GREEN-FOODS-GROCERY.COM\n"


        receipt += divider
        receipt += "\nCHECKOUT AT: " + readable_timestamp() + "\n"
        receipt += divider

     
        #Print Individual Items and Prices
       
        receipt += "\nSELECTED PRODUCT:"
        
        
        
        for selected_id in selected_ids:
                
            matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
            matching_product = matching_products[0]

           
            #Price per item IDs
            if matching_product["price_per"] == "N":
                
                name = find_id_name(matching_product)
                total_price = total_price + matching_product["price"]
            
            
                price_usd = "(" + to_usd(matching_product["price"]) + ")"
                    
               
                receipt += "\n... " + name + " " + price_usd


            #Price by pound IDs 
            elif matching_product["price_per"] == "Y":
            
                new_pound_price = matching_product["price"] * lbs[x]
                total_price = total_price + new_pound_price

                price_usd = to_usd(new_pound_price)
        
              
                receipt += "\n... " + name + " " + price_usd
                x = x + 1 
            
          



        
        receipt += "\n"
        receipt += divider

        #Calculate subtotal
        total_usd = to_usd(total_price)
        
     
        receipt += "\nSUBTOTAL: " + total_usd

        #Calculate tax
        load_dotenv()
        env_tax = os.environ.get("TAX_RATE")
        float_env_tax = float(env_tax)
        tax_amnt = total_price * float_env_tax
        tax_usd = to_usd(tax_amnt)
      
        receipt += "\nTAX: " + tax_usd


        #Calculate total
        tax_plus_total = tax_amnt + total_price
        tax_plus_total_usd = to_usd(tax_plus_total)
    
        receipt += "\nTOTAL: " + tax_plus_total_usd
    

        print_message("THANK YOU! SEE YOU AGAIN SOON!")
 
        
        receipt += "\n"
        receipt +=divider
        receipt += "\nTHANK YOU! SEE YOU AGAIN SOON!\n"
        receipt +=divider

        print(receipt)

        file.write(receipt)

