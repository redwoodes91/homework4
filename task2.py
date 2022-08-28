s = input("Введіть номер: ")
if not s.isdigit():
    print("введіть тільки числа")
elif len(s) != 10:
    print("номер має 10 цифр")

else:
    print("номер вірного формату")
