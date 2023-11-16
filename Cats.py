import random
import string
from itertools import permutations

word_dict = []
def numbersRound():
    print("It's time for a NUMBERS ROUND!")
    spaces = 6
    possibleLarge = [50, 25, 10, 75, 100]

    smallArr = []
    largeArr = []
    
    while(len(smallArr) + len(largeArr) < spaces):
        # Get num Small numbers
        while(True):
            print('How many small numbers would you like?')
            numSmall = input()
            print('You picked ' + numSmall + ' small numbers!')
            numSmall = int(numSmall)

            if(numSmall > spaces or len(smallArr) + len(largeArr) + numSmall > spaces):
                print('Too many! Try again')
                continue
            else:
                break

        # For loop to select
        for x in range(int(numSmall)):
            randomSmall = random.randint(0, 10)
            smallArr.append(randomSmall)
        
        # Check to see if it is done (all spaces filled)
        if(len(smallArr) + len(largeArr) >= spaces ):
            break

        # Get num Large numbers
        while(True):
            print('How many large numbers would you like?')
            numLarge = input()
            print('You picked ' + numLarge + ' large numbers!')
            numLarge = int(numLarge)

            if(numLarge > spaces or len(smallArr) + len(largeArr) + numLarge > spaces):
                print('Too many! Try again')
                continue
            else:
                break

        # For loop to select
        for x in range(int(numLarge)):
            index = random.randint(0, 4)
            randomLarge = possibleLarge[index]
            largeArr.append(randomLarge)
    
    totalSelections = smallArr + largeArr
    if(len(totalSelections) > spaces):
        print('You selected too many numbers! Getting rid of some...')
        for x in range(len(totalSelections) - spaces):
            totalSelections.pop(random.randint(0, len(totalSelections) - 1))
    print('Your selection is: ')
    print(totalSelections)

    print("Now... let's take a look at the number to generate...")
    goalNum = random.randint(100, 999)
    print(goalNum)


    # Do a TIMER
    # Find the best algo to brute force the solution
        # https://stackoverflow.com/questions/48655612/find-all-numbers-that-sum-closest-to-a-given-number-python

def makeDict():
    f = open("words_alpha.txt","r")
    word = f.readline()
    for word in f:
        word_dict.append(word)
        word = f.readline
    f.close()

def solveWordGame(dictionary, letters):
    print("Solving...")
    test = list(permutations(letters))
    print(test)

def lettersRound():
    print('LET')
    spaces = 9

    consonants = []
    vowels = []

    possibleVowels = ['A', 'E', 'I', 'O', 'U']

    while(len(consonants) + len(vowels) < spaces):
        # Get num consonants
        while(True):
            print('How many consonants would you like?')
            numCons = input()
            print('You picked ' + numCons + ' consonants!')
            numCons = int(numCons)

            if(numCons >= spaces or len(consonants) + len(vowels) + numCons > spaces):
                print('Too many! Try again')
                continue
            else:
                break

        # For loop to select
        for x in range(int(numCons)):
            choiceLetter = random.choice(string.ascii_uppercase)
            while choiceLetter in possibleVowels:
                choiceLetter = random.choice(string.ascii_uppercase)
                continue
            consonants.append(choiceLetter)
        
        # Check to see if it is done (all spaces filled)
        if(len(consonants) + len(vowels) >= spaces ):
            break

        # Get num vowels
        while(True):
            print('How many vowels would you like?')
            numVow = input()
            print('You picked ' + numVow + ' vowels!')
            numVow = int(numVow)

            if(numVow >= spaces or len(consonants) + len(vowels) + numVow > spaces):
                print('Too many! Try again')
                continue
            else:
                break

        # For loop to select
        for x in range(int(numVow)):
            choiceLetter = possibleVowels[random.randint(0, 4)]
            vowels.append(choiceLetter)

        # Check to see if it is done (all spaces filled)
        if((len(consonants) + len(vowels)) >= spaces ):
            break

    totalSelections = consonants + vowels
    print(totalSelections)

    solveWordGame(word_dict, totalSelections)
    


def play():
    print('PlayTime')

    #numbersRound()

    makeDict()
    lettersRound()


play()