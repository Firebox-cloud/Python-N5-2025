students = int(input("How many students?"))
Pizza = round(students/8) + 1
print("The total number of pizzas needed is: " + str (Pizza))
PizzaPrice = 12
total = Pizza * PizzaPrice
print("The total cost of the pizzas is: £" + str(total))