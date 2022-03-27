guess = ""
secret_word = "mulher"
tries = 0
tries_limit = 3

while guess != secret_word and tries < tries_limit:
    guess = input("Enter guess: ")
    tries += 1

print(f"Number of tries: {tries}")
if tries < tries_limit:
    print("You win")
else:
    print("Shit, you lose")
