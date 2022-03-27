import datetime
from ntpath import join


try:
    register_log = input("Enter your register log >> ")
    register_log = "{date} {separator} {register}".format(date = datetime.date.today(), separator =  "==>", register = register_log)
    register_log_file = open("data/register_log.txt", "a")
    register_log_file.write(register_log)
    register_log_file.close()
    print("Registered!")
except FileNotFoundError:
    print("File not found!")