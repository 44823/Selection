#Matthew Beer
#28/09/2014
#Development exercise 2 - Selection

temp1 = int(input("Please enter the temperature of water "))
if temp1 < 0:
    print("The water is frozen")
elif temp1 > 100:
    print("The water is boiling")
else: print("The water is neither frozen or boiling")
