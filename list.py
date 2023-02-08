fruits = ['Apple', 'Banana', 'Citrus', 'Kiwi', 'Mango', 'apple', 'mango', 'banana']
data = ['A', 'B', 'C', 1, 2, True, False, ['list', 'within', 'list'], 3.14, 0.14, None ]
numbers = [1,6,8,4,5]

for i in fruits:
    print(i)

for idx, fruit in enumerate(fruits):
  print(idx, fruit)

print(data[7])
print(data[7][1])
print(data[7][1][0])
print(fruits[0:4])
print(fruits[:-2])
print(fruits[-2])

fruits[0] = 'Apricot'

print(fruits)

fruits.append("grape")

print(fruits)

fruits.insert(3,"StrawBerry")
print(fruits)

fruits.remove('Mango')
del fruits[0]
print(fruits)

print(data.index(None))

print(fruits)
fruits.reverse()
print(fruits)

numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

fruits.sort()
print(fruits)

fruits.sort(key=str.lower)
print(fruits)


