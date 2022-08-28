s = input("Введіть: ")
s1 = s[:2] + s[-2:]
if len(s) < 2:
    print("Empty String")
else:
    print(s1)