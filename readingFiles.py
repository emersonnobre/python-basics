try:
    users_file = open("data/users.json", "r")

    if users_file.readable():
        print(users_file.read())
    else:
        print("This file is not acessible for reading mode")

    users_file.close()
except FileNotFoundError:
    print("The file path was not found!")