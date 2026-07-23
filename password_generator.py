import random
print()
print("Welcome to the password generator!")
print("This program will create 5 password options for you to choose from.")
print()
# ASKING USERS
length = int(input("Enter a number: "))
type = input("Enter password type (strong/medium/weak): ")

#charecters
strong = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
medium = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
weak = "abcdefghijklmnopqrstuvwxyz1234567890"


# GENERATING PASSWORDS
if type == "strong":
    charecter = strong
elif type == "medium":
    charecter = medium
else :
    charecter = weak

for i in range (10):
    password = ""
    for j in range (length):
        password += random.choice(charecter)
    print(password)
