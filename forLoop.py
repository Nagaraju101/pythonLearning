
arrString = ['naga', 'raju', 'nagaraju', 'ankamreddi', 'king', 'raja']

for name in arrString:
    if name == 'king':
        break
    print(name)


# When for loop has one string only, then it separates into toCharArray
data = 'Nagaraju'
for ch in data:
    if ch == 'r':
        break
    print('Current value is ---> ', ch)

# range(5) 0,1,2,3,4
for i in range(5):
    if i == 3 :
        break
    print(i)

#range(10, 20)  10 is starting point and 20 is ending point
for i in range(10,20):
    if i == 17 :
        break
    print(i)

#range(10, 20)  10 is starting point and 20 is ending point and 2 skip one number
for i in range(10,20,2):
    if i == 18 :
        break
    print(i)    
