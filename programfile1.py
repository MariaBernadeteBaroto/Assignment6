
# 1. Ask for four numbers


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
number4 = int(input("Enter fourth number: "))

# condtion 1
if number1 > number2:
    low1 = number2
    high1 = number1
else:
    low1 = number1
    high1 = number2

if number3 > number4:
    low2 = number4
    high2 = number3
else:
    low2 = number3
    high2 = number4

if low1 > low2:
    middle1 = low1
    lowest = low2
else:
    middle1 = low2
    lowest = low1

if high1 > high2:
    middle2 = high2
    highest = high1
else:
    middle2 = high1
    highest = high2

if middle2 > middle1:
    print (highest, middle2, middle1, lowest)
else:
    print(highest, middle1, middle2, lowest)

            


