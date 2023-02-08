def test1():
    a = 'Local test 1'
    print(a)

def test2():
    a = 'Local test 2'
    print(a)

def test3():
    a = 'Local test 3'
    test1()
    test2()


a = 'Global'
test3()
print(a)