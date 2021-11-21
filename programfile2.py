# generate two numbers

name = input('Enter your name: ')

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

add7 = random.randrange(0,99)
add8 = random.randrange(0,99)

answer4 = float(input(f'{add7} and {add8}: '))

if answer4 == add7 + add8:
    correct_asnwers4 = answer4
else: 
    uncorrect_answers4 = answer4

add9 = random.randrange(0,99)
add10 = random.randrange(0,99)

answer5 = float(input(f'{add9} and {add10}: '))

if answer5 == add9 + add10:
    correct_answer5 = answer5
else: 
    uncorrect_answers5 = answer5

add11 = random.randrange(0,99)
add12 = random.randrange(0,99)

answer6 = float(input(f'{add11} and {add12}: '))

if answer6 == add11 + add12:
    correct_answers6 = answer6
else:
    uncorrect_answers6 = answer6

add13 = random.randrange(0,99)
add14 = random.randrange(0,99)

answer7 = float(input(f'{add13} and {add14}: '))

if answer7 == add13 + add14:
    correct_answers7 = answer7
else:
    uncorrect_answer7 = answer7

add15 = random.randrange(0,99)
add16 = random.randrange(0,99)

answer8 = float(input(f'{add15} and {add16}: '))

if answer8 == add15 + add16:
    correct_answers8 = answer8
else:
    uncorrect_answers8 = answer8

add17 = random.randrange(0,99)
add18 = random.randrange(0,99)

answer9 = float(input(f'{add17} and {add18}: '))

if answer9 == add17 + add18:
    correct_answers9 = answer9
else:
    uncorrect_answers9 = answer9

add19 = random.randrange(0,99)
add20 = random.randrange(0,99)

answer10 = float(input(f'{add19} and {add20}: '))

if answer10 == add19 + add20:
    correct_answers10 = answer10
else:
    uncorrect_answer10 = answer10

correct_answers = (correct_answers1 + correct_asnwers2 + correct_answers3 + correct_asnwers4 + correct_answer5 + correct_answers6 + correct_answers7 +  correct_answers8 + correct_answers9 + correct_answers10 )


print(score)
print(name)






