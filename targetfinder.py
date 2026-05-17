n = list(map(int, input().split()))
target = int(input())
count = 0
for i in n:
    if i >target:
        count += 1
if count >= 3:
    print("pass")
else:
    print("fail")