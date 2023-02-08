laptop = {'brand':'Apple', 'model': 'MacBook Pro', 'size':  13}

for i in laptop.keys():
  print(i)

print("----------")

for i in laptop.values():
  print(i)

print("----------")

for i in laptop.items():
  print(i)

print("----------")

for i,j in laptop.items():
  print(i,j)


print (laptop)
print(laptop['brand'])


laptop['size']= 15

print(laptop)

laptop.update ( {'model': 'MacBook air', 'size':  15, 'year': 2015})
print('length of laptop dictionary is : ' , len(laptop))

print(laptop)

del laptop['year']

print(laptop)

# Pop return a value for the value which value was deleted
val = laptop.pop('size')
print('size', val)

print(laptop)
print(len(laptop))

# if we pass in NO Key or value exist in the dictionary. We need call it this way

print(laptop.get('color'))
print(laptop.get('color', 'Key Not Found!!'))
print(laptop.get('brand', 'Key Not Found!!'))

print(laptop.setdefault('color', 'silver'))