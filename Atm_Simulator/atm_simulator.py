print("=" * 30)
print("     ATM Simulator")
print("=" * 30)

# Ask user for initial balance
while True:
    try:
        balance = int(input("Please enter your starting balance: "))
        if balance < 0:
            print("Starting balance cannot be negative. Please enter a non-negative amount.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number for your balance.")

while True:
  print("\n1. Check Balance")
  print("2. Deposit Money")
  print("3. Withdraw Money")
  print("4. Exit ")

  choice = input("Enter Choice: (1-4) ")

  if choice == "1":
    print("\n---- Your Balance ----")
    print(f"Current Balance: ${balance}") # Corrected: Display current balance
    print("\n-----------------------------")

  elif choice == "2":
    try:
      print("\n----- Deposit Money-----")
      deposit_amount = int(input("\nEnter Money to Deposit: "))
      if deposit_amount > 0:
        balance += deposit_amount
        print(f"Deposit successful. New balance: ${balance}")
        print("\n--------------------------------------------")
      else:
        print("Deposit amount must be positive.")
        print("\n--------------------------------------------")
    except ValueError:
      print("Invalid input. Please enter a valid number.")
      print("\n--------------------------------------------")

  elif choice == "3":
    print("\n--------- Withdraw  Money -------------")
    try:
      withdraw_amount = int(input("\nEnter Money to Withdraw: "))
      if withdraw_amount > 0:
        if withdraw_amount <= balance:
          balance -= withdraw_amount
          print(f"Withdrawal successful. Withdrew: ${withdraw_amount}, New balance: ${balance}")
          print("\n--------------------------------------------")
        else:
          print("Insufficient balance.")
          print(f"Current Balance: ${balance}")
          print("\n--------------------------------------------")
      else:
        print("Withdrawal amount must be positive.")
        print("\n--------------------------------------------")
    except ValueError:
      print("Invalid input. Please enter a valid number.")
      print("\n--------------------------------------------")

  elif choice == "4":
    print("\n" + "=" * 44+"\n" )
    print("Exiting the program, Thank you for using !")
    print("\n" + "=" * 44)
    break

  else:
    print("Invalid choice. Please enter a number between 1 and 4.")