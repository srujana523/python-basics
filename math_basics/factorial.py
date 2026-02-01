def run_factorial():
    # We put your exact code inside here!
    n = int(input("Enter a number:"))
    fact = 1
    for x in range(1, (n + 1)):
        fact = fact * x
    print("The factorial of", n, "is", fact)