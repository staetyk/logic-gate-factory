import getGates

def test_get_0001_1_1():
    x = getGates.get("0001")
    assert x(1, 1) == 1
    
def test_get_10000001_0_0_1():
    with pytest.raises(Exception):
        x = getGates.get("10000001")
        x(0, 0) == 0

def test_get_1001101001011011():
    assert getGates.get("1001101001011011")(1,0,1,0) == 0

def test_get_not():
    assert getGates.get("10")(1) == 0