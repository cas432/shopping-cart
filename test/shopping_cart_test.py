from app.shopping_cart import to_usd, calc_tax, calc_total, filename_timestamp,readable_timestamp, find_product
from datetime import datetime
import pytest

def test_to_usd():
    # it should apply USD formatting
    assert to_usd(4.50) == "$4.50"

    # it should display two decimal places
    assert to_usd(4.5) == "$4.50"

    # it should round to two places
    assert to_usd(4.55555) == "$4.56"

    # it should display thousands separators
    assert to_usd(1234567890.5555555) == "$1,234,567,890.56"


def test_calc_tax():

    result = calc_tax(1000)
    assert result == 87.5


def test_calc_total():

    result = calc_total(112.6,20.3)
    assert result == 132.9


def test_filename_timestamp():
    
    filename = filename_timestamp()
    assert filename == datetime.now().strftime("%Y-%m-%d-%H-%M-%S")


def test_readable_timestamp():
    
    readable = readable_timestamp()
    assert readable == datetime.now().strftime("%Y-%m-%d %I:%M %p")
           

def test_find_product():

    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    ]

    # if there is a match, it should find and return a product
    matching_product = find_product("2", products)
    assert matching_product["name"] == "All-Seasons Salt"

    # if there is no match, it should raise an IndexError
    with pytest.raises(IndexError):
        find_product("2222", products)

