print("--- Welcome to Srujana's Math Tool ---")
print("1. Check Even or Odd")
print("2. Factorial (Coming soon!)")

# This line takes your input from the keyboard
choice = input("Select an option (1 or 2): ")

if choice == "1":
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Result: This is an EVEN number.")
    else:
        print("Result: This is an ODD number.")
elif choice == "2":
    print("You selected Factorial! We will connect your math_basics folder here next.")
else:
    print("Invalid input. Please run again and pick 1 or 2.")