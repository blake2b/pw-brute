import random
import string
import sys

print("You may exit the process at any time with CTRL+C")
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=+_/\{}';.,[]`"
chars_list = list(chars)
password = input("Enter a password: ")
tries = 0
guess_password = ""

try:
    while guess_password != password:
        guess_password = random.choices(chars_list, k=len(password))
        tries += int(1)

        print("Try ", tries, " => ", guess_password)

        if guess_password == list(password):
            print("Your password is: " + "".join(guess_password))
            input("Press enter to exit ")
            break

except KeyboardInterrupt:
    sys.exit()
