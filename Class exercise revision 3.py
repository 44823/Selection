#Matthew Beer
#28/09/2014
#Revision exercise 3 - Selection

num1 = int(input("Please enter a number between 21 and 29 "))
if num1 < 21:
    print("The number you have chosen is below the range")
elif 29 >= num1 >= 21:
    print("The number you have chosen is within the range")
elif num1 > 29:
    print("The number you have chosen is above the range")
