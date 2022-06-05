import random

gues_num = random.randint(1, 51)
print('Guess a number btw 1 and 50 or enter -1 to quit')
counter = 0

while True:
    counter += 1
    try:
        guessed_number = int(input('Enter the number: '))
    except ValueError as e:
        print('I said a number and you entered', e)
        continue
    if guessed_number == -1:
        print("Quitting game on user's request...")
        break
    if guessed_number == gues_num:
        print(f'You won in {counter} attempts\n')
        continuation = (input('Do you want to play again? Enter y to contiunue or anything else to quit: '))

        if continuation == "y" or continuation == "Y":
            gues_num = random.randint(1, 51)
            counter = 0

            continue
        elif continuation != "y" or continuation != "Y":
            break
    if guessed_number > gues_num and guessed_number <= 50:  # coz break above quits the program
        print('too much')
        continue
    if guessed_number < gues_num and guessed_number > 0:
        print('too little')
        continue
    if guessed_number == 0 or guessed_number < -1 or guessed_number > 50:
        print('Between 1 and 50 I said...')
        continue

print('Bye bye!')
