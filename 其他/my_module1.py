__all__ = ['test_b']  # 被导入时，只能用test_b,不能用test_a

def test_a(a,b):
    print(a + b)

def test_b(a,b):
    print(a - b)

