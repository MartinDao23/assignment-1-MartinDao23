# Your solution comes here
a = int(input("Enter number"))
b = int(input("Enter number"))
c = int(input("Enter number"))
s = int(input("Amount? "))
if s <= a:
    print(s)
elif s <= b:
    s *= 0.1
elif s <= c:
    s *= 0.25
else:
    s *= 0.5
print(s)