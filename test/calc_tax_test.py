from app.shopping_cart import calc_tax
def test_calc_tax():

    result = calc_tax(1000)
    assert result == 87.5
