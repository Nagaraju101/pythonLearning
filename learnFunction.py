def learnFunc(name):
    print("Invoking this function")
    print('Given name is :', name )
    return name

print("Hello there .... We are learning python functions: ")

result  = learnFunc("nagaraju")
print('result: ', result)


def countVowles(given_string):
    cnt = 0
    for ch in given_string:
      if ch.upper() in ("A", "E", "I", "O" "U"):
         cnt += 1
    return cnt

name = input('What is your name?  ')
result = countVowles(name)
print(result)