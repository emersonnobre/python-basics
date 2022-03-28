try:
    number = int(input("Enter a number: "))
    division = 10/number
    print(division)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid input")
finally:
    print("Esse trecho sempre será executado")

# geralmente usado para debugar o código, se não conferir irá estourar
# um erro com a mensagem especificada
assert number != 0, "Erro de divisão por zero!"
result = 10/number