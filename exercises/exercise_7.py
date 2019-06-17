#gussing game
import random
correct_answer = random.randrange(10)
user_answer = 0
turns = 3

while correct_answer != user_answer and turns > 0:
    temp_answer = input('Guess: ')
    user_answer = int(temp_answer)
    turns -= 1
    if user_answer == correct_answer:
        print('Correct!')
        break
    elif turns == 0:
        print('Game Over')
    elif user_answer > correct_answer:
        print(f'Go lower, {turns} turns left.')
    elif user_answer < correct_answer:
        print(f'Go higher, {turns} turns left.')
else:
    print(f'Correct answer was {correct_answer}')