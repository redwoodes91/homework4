s = input("3 + 5 = ")
if not s.isdigit():
    print("тільки число!")
elif int(s) == 3 + 5:
    print("відповідь вірна")
else:
    print("невірна відповідь")

