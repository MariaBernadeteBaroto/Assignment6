# generate two numbers

import random 

# generate two numbers 

add1 = random.randrange(0,99)
add2 = random.randrange(0,99)

answer1 = float(input(f'find the sum of {add1} and {add2}: '))

import math
if answer1 == add1 + add2:
    correct_answers1 = answer1
else:
    incorrect_answers1 = answer1

add3 = random.randrange(0,99)
add4 = random.randrange(0,99)

answer2 = float(input(f'{add3} and {add4}: '))

if answer2 == add3 + add4:
    correct_asnwers2 = answer2
else:
    incorrect_answer2 = answer2

add5 = random.randrange(0,99)
add6 = random.randrange(0,99)

answer3 = input(f'{add5} and {add6}: ')

if answer3 == add5 + add6:
    correct_answers3 = answer3
else:
    incorrect_answers3 = answer3




