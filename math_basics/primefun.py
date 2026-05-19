def prime(n):
    if n <=1:
            return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i+=1
    return True
n = int(input())
if(prime(n)):
     print("n is a prime number")
else:
     print("n is not a prime number")
