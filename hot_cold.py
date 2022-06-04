import random

gues_num = random.randint(1, 51)
print(gues_num)
still_playing = True
print('Guess a number btw 1 and 50 or enter -1 to quit')
counter = 0
while still_playing:
    counter += 1
    try:
        temp = int(input('Enter the number: '))
    except ValueError as e:
        print('I said a number and you entered', e)
        continue
    if temp == -1:
        print("Quitting game on user's request...")
        still_playing = False
    if temp == gues_num:
        print(f'You won in {counter} attempts')
        break
    if temp > gues_num and temp <= 50:  # coz break above quits the program
        print('too much')
        continue
    if temp < gues_num and temp > 0:
        print('too little')
        continue
    if temp == 0 or temp < -1 or temp > 50:
        print('Between 1 and 50 I said...')
        continue

print('Bye bye!')
