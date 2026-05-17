n = list(map(int, input().split()))
total = 0
for i in n:
    if i % 3 == 0: # Check if the number is divisible by 3
        total = total+i
print(total)