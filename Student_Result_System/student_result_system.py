# Student Result System

print("=" * 30)
print("  Student Result System  ")
print("=" * 30)

def student_information():
  name = (input("\nEnter Your Name: "))

  eng_mrks = int(input("\nEnter English Marks: "))
  math_mrks = int(input("Enter Math Marks: "))
  science_mrks = int(input("Enter Science Marks: "))

  print("\n" + "=" * 30)
  print("  Student Report  ")
  print("=" * 30)

  print(f"\nName      : {name} ")
  print(f"English   : {eng_mrks}")
  print(f"Math      : {math_mrks}")
  print(f"Science   : {science_mrks}")

  calculate(eng_mrks, math_mrks, science_mrks)

def calculate(eng_mrks, math_mrks, science_mrks):
  total_marks = eng_mrks + math_mrks + science_mrks
  print(f"\nTotal Marks : {total_marks}")

  average(eng_mrks, math_mrks, science_mrks)

def average(eng_mrks, math_mrks, science_mrks):
  average_marks = (eng_mrks + math_mrks + science_mrks) / 3
  print(f"Average Marks : {average_marks}")

  # Pass average_marks to the grade function
  grade(average_marks)

def grade(average_marks):
  if average_marks >= 90:
    print("Grade: A+")
  elif average_marks >= 80:
    print("Grade: A")
  elif average_marks >= 70:
    print("Grade: B")
  elif average_marks >= 60:
    print("Grade: C")
  elif average_marks >= 50:
    print("Grade: D")
  else:
    print("Grade: F")
    print("Do it better next time! Keep studying hard.")

student_information()