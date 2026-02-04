history = []
while True:
    print("welcome to study log")
    law = float(input("How many hours did you prepare for lawcet today?"))
    shorthand = float(input("How many hours did you prepare for shorthand today?"))
    coding = float(input("How many hours did you prepare for coding today?"))
    total = law+shorthand+coding
    entry = {
        "law": law,
        "shorthand": shorthand,
        "coding": coding,
        "total": total
    }
    history.append(entry) #adds total to the memory list
    print(f"\nTotal study time: {total}hours")
    if total >=5:
        print("Result:Excellent you are on track")
    elif total >=3:
        print("Result:Well done you did a great job")
    else:
        print("Result:Tomorrow is a great day,Lets aim for more!")
    stay = input("Do you want to track for another day:Yes/No?")
    if stay.capitalize() == "No":
        print("Okay,Bye!")
        break
if history:
    print("\n" + "="*45)
    print("        DETAILED SESSION REPORT")
    print("="*45)
    
    # This loop goes through the notebook and prints every page
    for i, data in enumerate(history, 1):
        print(f"Entry {i}: Law {data['law']}h | Short {data['shorthand']}h | Code {data['coding']}h")
    
    # Calculating the average from the 'total' inside each dictionary
    all_totals = [d['total'] for d in history]
    average = sum(all_totals) / len(all_totals)
    
    print("-" * 45)
    print(f"Session Average: {average:.2f} hours")
    print(f"Total Days Tracked: {len(history)}")
    print("\nKeep up the great work. Bye!")