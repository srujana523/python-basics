def count_them(arr):
    count =0
    for i in arr:
        if i > 5:
            count+=1
    return count
arr = list(map(int, input().split()))
print(count_them(arr))