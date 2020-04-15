from app.shopping_cart import find_id_name

def find_id():

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price_per": "N"}
]
    #Check for correct name
    result1 = find_id_name(products)["name"]
   
    assert result1 == "Chocolate Sandwich Cookies"


def find_id_name(my_id):
    return my_id["name"]