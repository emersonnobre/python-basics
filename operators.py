# Operadores de identidade
# Comparam os endereços de memória entre duas variáveis

a = 10
c = 10
b = a 

print(b is a) # true
print(c is a) # true

# Quando mudamos o valor de b ele passa a apontar para um local diferente
# de a.
b += 23

print(b is a)

# Operadores de Membership

list = [1, 2, 3, 4]
a = 40
b = 3

print(a in list) # False
print(b not in list) # False

# Ternary operator

print(a, "is greater") if a > b else print(b, "is greater")

# Operator overloading: um operador pode fazer mais que uma coisa
print(3 * 3)
print("Eu"*8)