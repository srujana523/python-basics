while True:
    print("welcome to study log")
    law = float(input("How many hours did you prepare for lawcet today?"))
    shorthand = float(input("How many hours did you prepare for shorthand today?"))
    coding = float(input("How many hours did you prepare for coding today?"))
    total = law+shorthand+coding
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

