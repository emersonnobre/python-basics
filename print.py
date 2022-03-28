from datetime import datetime

register_log_file = None

try:
    register_log_file = open("data/register_log.txt", "r+")
    register = str(datetime.today()) + " || " + "Type the register >> 0"
    print(register, file=register_log_file)
    register_log_file.close()
except FileNotFoundError:
    print("The file was not found") 

print("Some content", end="@@\n")

# print sem usar for para arrays (dica top)

l = [2, 4, 2, 4, 3]

print(*l)

# Formatando as saídas com o module operator (%)

print("First value: %2d and seconde value: %5.2f" % (43, 06.4433)) 

# Formatando as saídas com format

print("First value: {0} and second value: {1:5.1f}".format(12, 0.432))

# Print das informações de um dicionaŕio

data = dict(name = "Brenda", verb = "love")
print("I {verb} {name}".format(**data))

# Print centralzando a mensagem no meio, na esquerda e direita

center_string = "I love geeksforgeeks"

print(center_string.center(40, '#'))

print(center_string.ljust(40, '-'))

print(center_string.rjust(40, '-'))