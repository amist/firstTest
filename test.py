from code import Code

def test_sum():
    c = Code()
    assert c.sum(1,2) == 3
    
    
def test_all():
    test_sum()
    
    
if __name__ == '__main__':
    test_all()