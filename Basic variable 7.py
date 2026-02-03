overdue = int(input("How many days is your book overdue"))
fine_per_book = 0.50
total_fine = overdue * fine_per_book
if overdue > 5:
    total_fine = total_fine + 2.00

    print("The total fine for overdue books is: £" + str(round(total_fine,)))