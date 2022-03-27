def sayhi(name):
    print(f"Hello, {name}!")

def powTo(value, power):
    return pow(value, power)

name = input("Enter your name: ")
value = float(input("Enter the number: "))
power = float(input("Enter the power: "))

result = powTo(value, power)
sayhi(name)
print(result)