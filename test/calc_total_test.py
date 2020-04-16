from app.shopping_cart import calc_total
def test_calc_total():

    result = calc_total(112.6,20.3)
    assert result == 132.9
