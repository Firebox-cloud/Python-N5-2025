# Temperature Tracker challenge
temps = []
loop = 5
for i in range (loop):
    temperature=int(input("Enter temperature in Celsuis: "))
    while temperature <-20 or temperature> 50:
        if temperature <-20:
            print("Must be higer than -20 degrees")
        elif temperature > 50:
            print("Must be lower than 50 degrees")
        temperature=int(input("Enter temperature in Celsuis: "))
    temps.append(temperature)
print('Average temperature is: ', sum(temps)/loop )