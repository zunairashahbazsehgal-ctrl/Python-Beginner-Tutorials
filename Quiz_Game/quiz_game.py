while True:
    score = 0

    print("=" * 35)
    print("      PYTHON QUIZ GAME")
    print("=" * 35)

    # ---------------- Question 1 ----------------
    print("\nQuestion 1")
    print("What is the capital of Pakistan?")
    print("1. Karachi")
    print("2. Lahore")
    print("3. Islamabad")
    print("4. Peshawar")

    answer = input("\nEnter your answer (1-4): ")

    if answer == "3":
        print("Correct!")
        score += 2
    elif answer in ["1", "2", "4"]:
        print("Incorrect!")
        print("Correct Answer: Islamabad")
    else:
        print("Invalid input!")
        print("Correct Answer: Islamabad")

    # ---------------- Question 2 ----------------
    print("\nQuestion 2")
    print("Which keyword is used to create a function in Python?")
    print("1. function")
    print("2. def")
    print("3. create")
    print("4. func")

    answer = input("\nEnter your answer (1-4): ")

    if answer == "2":
        print("Correct!")
        score += 2
    elif answer in ["1", "3", "4"]:
        print("Incorrect!")
        print("Correct Answer: def")
    else:
        print("Invalid input!")
        print("Correct Answer: def")

    # ---------------- Final Score ----------------
    print("\n" + "=" * 35)
    print(f"Quiz Finished!")
    print(f"Your Final Score: {score}/4")
    print("=" * 35)

    # ---------------- Play Again ----------------
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

    if play_again == "yes":
        print()
        continue
    else:
        print("\nThank you for playing!")
        break