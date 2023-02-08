print("Hello there!!")

print("Please enter your first name: ")
first_name = input()
first_name_length = len(first_name)

print("Enter your last name now : ")
last_name = input()
last_name_length = len(last_name)

if(first_name_length < last_name_length):
    print("Your first name is shorter then last name")
elif(first_name_length > last_name_length):
    print("Your last name is shorter than first name ")
else:
    print("Your first and last name have the same length")
