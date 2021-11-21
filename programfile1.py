
# 1. Ask for four numbers


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
number4 = int(input("Enter fourth number: "))

# condtion 1
def sort4_descending(number1, number2,number3, number4):
    if number1 > number2:
        if number2> number3:
            if number4 > number2:
                if number4 > number1:
                    return (number4, number1, number2, number3)
                else:
                    if number4 > number3:
                        return(number1, number2, number4, number3)
                    else:
                        return(number1, number2, number3, number4)

            


