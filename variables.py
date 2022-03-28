# É uma linguagem fracamente tipada e não precisa de palavras-chave para declarar variáveis
name = input("Tell me your name: ")
print(f"Hello, {name.capitalize()}!")

# Conditional operator (one liner ifelse)
# variavel = {valor se for verdadeiro} if {condicao} else {valor se for falso}
valor = True if 20 > 10 else False

# Pegando vários valores em um input com split e convertendo com list/map
coordinatex, coordinatey = list(map(int, input("Type the coordinates").split(" ", 2)))
print(coordinatex, coordinatey)

# Pegando vários valores em um input com list comprehension
valorx, valory = [int(value) for value in input("Type two values").split()]
