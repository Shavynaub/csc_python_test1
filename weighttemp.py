opp = input("Enter the following operation: kg, lbs, K, C, F")
val = float(input("Enter your value to be converted!"))

if opp == "kg":
    print(f"This is your vavlue in lbs: {val*2.2:.2f}")
elif opp == "lbs":
    print(f"This is your value in kg: {val/2.2:.2f}")
elif opp == "C":
    print(f"This is your value in F: {val*2.2+32:.2f}")
    print(f"This is your value in K: {val+273:.2f}")
elif opp == "F":
    print(f"This is your value in C: {val-32/2:.2f}")
    print(f"This is your value in K {}")
else:
    print("done")