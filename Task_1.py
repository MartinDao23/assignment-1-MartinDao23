# Your solution comes here
number = int(input("Enter a three digit number"))
ones = number%10
tens = (number//10)%10
hundreds = number//100
print(f"{ones}{tens}{hundreds}")