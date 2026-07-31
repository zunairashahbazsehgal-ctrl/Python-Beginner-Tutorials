import random

print()
print("Welcome To The Number Guessing Game")
print("Enter Numbers from 1 to 10")
print()

comp = random.randint(1, 10)

for attempt in range(1,6):
    print()
    print(f"Attempt {attempt}/5")
    

    try:
        num = int(input("Enter Number: "))
        
    except ValueError:
        print("Enter a number only please !")
        continue

    if num == comp:
        print("🎉 Congratulations!")
        print("You guessed the correct number:", comp)
        print()
        break
    elif num < comp:
        print("Too low, try again")
        print()
    else:
        print("Too high, try again")
        print()
else:
    print("Out of attempts! The number was", comp)





