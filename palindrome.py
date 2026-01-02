word = (input("Enter a word:"))
rev = word[::-1]
print (rev)
if  rev == word:
    print(word,"is palindrome")
else:
    print(word,"is not a palindrome")