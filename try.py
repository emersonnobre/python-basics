try:
    number = int(input("Enter a number: "))
    division = 10/number
    print(division)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid input")