# By ActiniumGod

import random, time
play = True
while play:
    guesstime = 0
    try:
        min = int(input("Please input the min number:"))
        max = int(input("Please input the max number:"))
    except:
        print("Please input a number.")
        continue
    if min >= max:
        print("The numbers are error, please input them again.")
        continue
    num = random.randint(min, max)
    win = False
    while win != True:
        try:
            ans = int(input("Please input the answer:"))
        except:
            print("Please input a number.")
            continue
        if ans > num:
            guesstime += 1
            print("The answer is too big, try lower.")
        elif ans < num:
            guesstime += 1
            print("The answer is too small, try higher.")
        else:
            guesstime += 1
            if guesstime > 1:
                print("You guess for %s times. The number is %s, you win the game." % (guesstime, num))
            elif guesstime == 1:
                print("You are lucky, the number is %s." % num)
            win = True
    ans = input("Do you want to play the game again? (Y/N)\n")
    if ans == 'y' or ans == 'Y':
        print("Play again.")
    elif ans == 'n' or ans == 'N':
        play = False
print("See you.")
time.sleep(1)
