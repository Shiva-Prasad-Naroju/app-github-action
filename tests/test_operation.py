from src.math_operations import add,sub

def test_add():
    assert add(3,4)==7
    assert add(2,2)==4

def test_sub():
    assert sub(4,3)==1
    assert sub(10,20)==-10
    assert sub(10,8)==2