import random

Mysteryfruits = ["apple", "banana", "blueberry", "kiwi", "mango" , "peach" , "pineapple" , "raspberry" , "strawberry"]
userfruits = []
counter = 0
decision = "yes"

while decision == "yes" and counter <6:
    userInput = input("Please enter your first fruit name")
    while len(userInput) <4:
        print("invalid fruit length")
        userInput = input("Please enter your first fruit name")
    userfruits.append(input)
    counter = counter + 1
    decision = input("Do you want to enter another fruit?")
    
number = random.randint(0,9)

for index in range (counter):
    print(userfruits[index])
print("The mystery fruit is", Mysteryfruits[number])
counter = counter + 1
if counter < 3:
    print("milkshake is recomeneded")
if counter == 3 or counter == 4:
    print("Smoothie is recommenend") 
if counter > 4:
    print("Fruit juice is recommenend")
