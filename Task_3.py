# Your solution comes here
number = int(input("Enter a three digit number"))
ones = number%10
tens = (number//10)%10
hundreds = number//100
sum_1_3 = ones + hundreds
if sum_1_3 < hundreds:
    print("<")
elif sum_1_3 == hundreds:
    print("=")
else:
    print(">")