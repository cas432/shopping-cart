from app.shopping_cart import filename_timestamp
from datetime import datetime

def test_filename_timestamp():
    
    filename = filename_timestamp()
    assert filename == datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
           

