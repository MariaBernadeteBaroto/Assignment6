# generate two numbers
import math
name = input('Enter your name: ')

direction = print('Direction: Find the sum of the numbers that will appear. ')

import random
score = 0
wrong = 0

add1 = random.randint(0,99)
add2 = random.randint(0,99)

answer1 = input('1. '+str(add1) +' + '+str(add2) +': ')
if float(answer1) == add1 + add2:
    print('correct')
    score = score + 1
else:
    print('wrong')
    wrong = wrong + 1

add3 = random.randint(0,99)
add4 = random.randint(0,99)

answer2 = input('2. '+str(add3) +' + '+str(add4) +': ')
if float(answer2) == add3 + add4:
    print('correct')
    score = score + 1
else:
    print('wrong')
    wrong = wrong + 1

add5 = random.randint(0,99)
add6 = random.randint(0,99)

answer3 = input('3. '+str(add5) +' + '+str(add6) +': ')
if float(answer3) == add5 + add6:
    print('correct')
    score = score + 1
else:
    print('wrong')
    wrong = wrong + 1

add7 = random.randint(0,99)
add8 = random.randint(0,99)

answer4 = input('4.'+str(add7) +' + '+str(add8) +': ')
if float(answer4) == add7 + add8:
    print('correct')
    score = score + 1
else:
    print('wrong')
    wrong = wrong + 1

add9 = random.randint(0,99)
add10 = random.randint(0,99)

answer5 = input('5. '+str(add9) +' + '+str(add10) +': ')
if float(answer5) == add9 + add10:
    print('correct')
    score = score + 1
else:
    print('wrong')
    wrong = wrong + 1

    



print('Your score is '+str(score) +' / 10')
print(name)









