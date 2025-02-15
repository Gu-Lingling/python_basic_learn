def test_return():
    return 1, 2, 3, 'hehahi', True # return里返回多个值

x, y, z, i, j = test_return()
print(x,y,z,i,j)