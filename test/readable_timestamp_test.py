from app.shopping_cart import readable_timestamp
from datetime import datetime

def test_readable_timestamp():
    
    readable = readable_timestamp()
    assert readable == datetime.now().strftime("%Y-%m-%d %I:%M %p")
           

