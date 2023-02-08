import sys
import webbrowser as wb
import datetime as dt, random as rn
import countVowels as cv

print("Today's date is : ", dt.date.today())
print("Picking random number from 0-10 : ", rn.randint(0,10))

name = input("Enter your name: " )
print(cv.countvowles(name))