# Program 3 - Invetigate and modify

password = input("Please enter your password:")

while len (password) > 8:
    print("Error, try again must be longer than 8 characters.")

    password = input("Please ennter your password:")

print("Password accepted")