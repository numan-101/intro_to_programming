# modules
# functions
# loop

import random

# global vars
turns = 10
score = 0

def generate_random(upper):
    r = random.randint(1, upper)
    return r

def main():
    global score 
    run = True
    num1 = generate_random(10)
    num2 = generate_random(10)
    result = num1 * num2
    while run:
        ans = input(f'What is {num1} x {num2} ? ')

        if ans.isdigit():
            if int(ans) == result:
                print('Correct!')
                run = False
                score += 1
            else:
                print('Incorrect, try again')
        else:
            print('Answer must be a number')

for x in range(turns):
    main()

print(f'score: {score}/10')