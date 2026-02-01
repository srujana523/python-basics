from math_basics import even_num
from math_basics import factorial
while True:
    print("--- Welcome to Srujana's Math Tool ---")
    print("1. Check Even or Odd")
    print("2. calculate Factorial")
    print("3. Exit")
    choice = input("Select an option (1,2 or 3): ")
    if choice == "1":
        even_num.even_odd()
    elif choice == "2":
        factorial.run_factorial()
    elif choice =="3":
        print("Goodbye! Thanks for using my tool.")
        break
    else:
        print("Invalid input. Please try again")