# Number guessing Game 

from numpy import random
import preferredsoundplayer as pr

def randomNum(a,b):
    x = random.randint(a,b)
    return x

def display(levelCounts):
    print('\n--------------------------Score Board -----------------------------')
    print('Level I Count:',levelCounts['FirstLevel'])
    print('Level II Count:',levelCounts['SecondLevel'])
    print('Level III Count:',levelCounts['ThirdLevel'])
    print('Total:',levelCounts['FirstLevel']+levelCounts['SecondLevel']+levelCounts['ThirdLevel'])

def levelFinal(levelCounts):
    print('\n--------------------------- Level III -------------------------------\nGuess the number between 1 to 1000')
    pr.soundplay("x_next-level-160613.mp3",1)
    x= randomNum(1,1001)
    count=0
    print('Enter x or X to Exit Game.........')
    pr.soundplay("going-to-the-next-level-114480.mp3",1)
    while(True):
        # print('\n Guess the number.........\n')
        userInput = input('\nGuess the number: ')
        if(userInput=='x' or userInput=='X'):
            print('\nThnak you for playing this game...........')
            pr.soundplay("8-bit-video-game-lose-sound-version-1-145828.mp3",1)
            break
            
        else:
            try:
                userInput=int(userInput)
                if(userInput>x):
                    count+=1
                    pr.soundplay("pop-sound-effect-197846.mp3",1)
                    print('Try Again! You guessed too high....')
                elif(userInput<x):
                    count+=1
                    pr.soundplay("pop-sound-effect-197846.mp3",1)
                    print('Try Again! You guessed too small....')
                elif(userInput==x):
                    count+=1
                    print('-----------You guessed Right Number: ',x ,'---------------')
                    print('Count: ',count)
                    levelCounts['ThirdLevel']=count
                    display(levelCounts)
                    pr.soundplay("game-bonus-144751.mp3",1)
                    break
            except :
                print('\nEnter the integer value only.......')
    return True


def levelmid(levelCounts):
    print('\n--------------------------- Level II -------------------------------\nGuess the number between 1 to 500')
    pr.soundplay("x_next-level-160613.mp3",1)
    x= randomNum(1,501)
    count=0
    print('Enter x or X to Exit Game.........')
    pr.soundplay("going-to-the-next-level-114480.mp3",1)
    while(True):
        # print('\n Guess the number.........\n')
        userInput = input('\nGuess the number: ')
        if(userInput=='x' or userInput=='X'):
            print('\nThnak you for playing this game...........')
            pr.soundplay("8-bit-video-game-lose-sound-version-1-145828.mp3",1)
            break
            
        else:
            try:
                userInput=int(userInput)
                if(userInput>x):
                    count+=1
                    pr.soundplay("pop-sound-effect-197846.mp3",1)
                    print('Try Again! You guessed too high....')
                elif(userInput<x):
                    count+=1
                    pr.soundplay("pop-sound-effect-197846.mp3",1)
                    print('Try Again! You guessed too small....')
                elif(userInput==x):
                    count+=1
                    print('-----------You guessed Right Number: ',x ,'---------------')
                    print('Count: ',count)
                    levelCounts['SecondLevel']=count
                    pr.soundplay("game-bonus-144751.mp3",1)
                    dec01 = levelFinal(levelCounts)
                    if(dec01 == True):
                        break
            except :
                print('\nEnter the integer value only.......')
    return True


if __name__ =='__main__':
    levelCounts = {}
    x = randomNum(1,101)
    print(x)
    count=0
    print('\n--------------------------- Level I -------------------------------\nGuess the number between 1 to 100')

    print('Enter x or X to Exit Game.........')
    pr.soundplay("going-to-the-next-level-114480.mp3",1)
    while(True):
        # print('\n Guess the number.........\n')
        userInput = input('\nGuess the number: ')
        if(userInput=='x' or userInput=='X'):
            print('\nThnak you for playing this game...........')
            pr.soundplay("8-bit-video-game-lose-sound-version-1-145828.mp3",1)
            break
        else:
            try:
                userInput=int(userInput)
                if(userInput>x):
                    count+=1
                    pr.soundplay("pop-sound-effect-197846.mp3",1)
                    print('Try Again! You guessed too high....')
                elif(userInput<x):
                    count+=1
                    pr.soundplay("pop-sound-effect-197846.mp3",1)
                    print('Try Again! You guessed too small....')
                elif(userInput==x):
                    count+=1
                    print('-----------You guessed Right Number: ',x ,'---------------')
                    print('Count: ',count)
                    levelCounts['FirstLevel']=count
                    pr.soundplay("game-bonus-144751.mp3",1)
                    dec = levelmid(levelCounts)
                    if(dec == True):
                        break
            except :
                print('\nEnter the integer value only.......')

