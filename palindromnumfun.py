def is_palindrome(n):
    original = n
    reversed_num = 0
    while n>0:
        digit = n % 10
        reversed_num = reversed_num *10 +digit
        n = n//10
    return original == reversed_num
num = int(input())
print(is_palindrome(num))