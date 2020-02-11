import datetime
from dotenv import load_dotenv
import os
 
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


#PART I: CAPTURE USER INPUT

#Initialize Variables/Lists

selected_ids = []
all_ids = []
lbs = []
total_price = 0
x = 0 #lbs index number 
divider = "-------------------------"


print("\nWELCOME!")

#Create list of all valid IDs
for p in products:
    Id_num =str(p["id"])
    all_ids.append(Id_num)

#Enter and Validate Inputs   
while True: 
    selected_id = input("Please input a product ID: ")
                
   
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

#Pull Date Info
from datetime import date
today = datetime.date.today().strftime("%Y-%m-%d")

#Pull Time Info
import time
hour = (time.strftime("%I:%M %p"))

#Create Receipt File
today_file_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
#file_path = "receipts/" + today_file_name + ".txt"
file_path = os.path.join(os.path.dirname(__file__), "receipts", today_file_name + ".txt")



#Print out Receipt/Write File
with open(file_path, "w") as file:

    print(divider)
    print("GREEN FOODS GROCERY")
    print("(123)-555-1234")
    print("WWW.GREEN-FOODS-GROCERY.COM")

    print(divider)
    print("CHECKOUT AT: " + today + " " + hour) 
    print(divider)

    file.write(divider)
    file.write("\nGREEN FOODS GROCERY\n")
    file.write("(123)-555-1234\n")
    file.write("WWW.GREEN-FOODS-GROCERY.COM\n")

    file.write(divider)
    file.write("\nCHECKOUT AT: " + today + " " + hour + "\n") 
    file.write(divider)

    #Print Individual Items and Prices
    print("SELECTED PRODUCT: ")
    file.write("\nSELECTED PRODUCT:")
    
    
    
    for selected_id in selected_ids:
            
        matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
         
        matching_product = matching_products[0]

        #Price per item IDs
        if matching_product["price_per"] == "N":
            total_price = total_price + matching_product["price"]
        
         
            price_usd = "(${0:.2f})".format(matching_product["price"])
                
            print("... " + matching_product["name"] + " " + price_usd)
            file.write("\n... " + matching_product["name"] + " " + price_usd)


        #Price by pound IDs 
        elif matching_product["price_per"] == "Y":
           
            new_pound_price = matching_product["price"] * lbs[x]
            total_price = total_price + new_pound_price

            price_usd = "(${0:.2f})".format(new_pound_price)
    
            print("... " + matching_product["name"] + " " + price_usd)
            file.write("\n... " + matching_product["name"] + " " + price_usd)
            x = x + 1


    
    file.write("\n")
    file.write(divider)

    #Calculate subtotal
    total_usd = "${0:.2f}".format(total_price)
    print(divider)
    print("SUBTOTAL: " + total_usd)
    file.write("\nSUBTOTAL: " + total_usd)

    #Calculate tax
    load_dotenv()
    env_tax = os.environ.get("TAX_RATE")
    float_env_tax = float(env_tax)
    tax_amnt = total_price * float_env_tax
    tax_usd = "${0:.2f}".format(tax_amnt)
    print("TAX: " + tax_usd)
    file.write("\nTAX: " + tax_usd)


    #Calculate total
    tax_plus_total = tax_amnt + total_price
    tax_plus_total_usd = "${0:.2f}".format(tax_plus_total)
    print("TOTAL: " + tax_plus_total_usd)
    file.write("\nTOTAL: " + tax_plus_total_usd)
  

    print(divider)
    print("THANK YOU! SEE YOU AGAIN SOON!")
    print(divider)
    
    file.write("\n")
    file.write(divider)
    file.write("\nTHANK YOU! SEE YOU AGAIN SOON!\n")
    file.write(divider)

