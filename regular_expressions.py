# regular expression to detect floating number
import re

floating_number = input("Enter a float number: ")

result = bool(re.match(r"^[-+]?[0-9]*\.[0-9]+$", floating_number))

if result:
    print("Floating Number")
else:
    print("Not a Floating Number")


# regular expression for email

email = input("Enter a e-mail address: ")

result = bool(re.match(r"^[a-zA-z0-9_\-.]+[@][a-zA-z0-9_\-.]+\.[a-zA-z]{2,5}$", email))

if result:
    print("E-mail")
else:
    print("Not a E-mail")
