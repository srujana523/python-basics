original_list = []
bank_balances = list(map(int, input().split()))
for balance in bank_balances:
 if balance<500:
   charges = balance - 25
   original_list.append(charges)
 else:
   original_list.append(balance)
print(original_list)