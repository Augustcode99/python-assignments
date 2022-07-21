#Task : Let's say; you left a message in the past that prints a password you need.
#To see the password you wrote, you need to enter your name and the program should recognize you.

name = input("enter your name for your password\n").title()
password = "W@12"

if name == "August":
    print(f"Hello, {name}! The password is : {password}")
else:
    print(f"Hello, {name}! See you later.")