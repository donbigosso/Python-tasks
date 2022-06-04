import random
gues_num = random.randint(1,51)
print(gues_num)
still_playing = True
print('Guess a number btw 1 and 50')
counter = 0
while still_playing:
    counter += 1
    temp = int(input('podaj liczbe\n'))
    if temp == -1:
        still_playing = False
    if temp == gues_num:
        print(f'You won in {counter} attempts')
        break
    if temp > gues_num:    #coz break above quits the program
        print('too much')
        continue
    print('too little')
    continue

print('end of program')