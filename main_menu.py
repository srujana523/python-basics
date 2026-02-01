from math_basics import even_num
from math_basics import factorial
print("--- Welcome to Srujana's Math Tool ---")
print("1. Check Even or Odd")
print("2. calculate Factorial")

# This line takes your input from the keyboard
choice = input("Select an option (1 or 2): ")

if choice == "1":
    even_num.even_odd()
elif choice == "2":
    factorial.run_factorial()
else:
    print("Invalid input. Please run again and pick 1 or 2.")