def sayhi(name):
    print(f"Hello, {name}!")

def powTo(value, power):
    return pow(value, power)

result = powTo(4, 4)
sayhi("Emerson")
print(result)

# lambda functions
multiplicaPorDois = lambda value: value * 2

print(multiplicaPorDois(8))