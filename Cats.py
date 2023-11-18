import random
import string
from itertools import permutations, chain, combinations, product

word_dict = set()

winningNums = []
winningOps = []
def solveNumbersGame(goal, selection):
    operations = ["A", "S", "M", "D"]
    operationsPerm = list(product(operations, repeat=5))

    selectionPerm = list(permutations(selection)) 

    for opList in operationsPerm:

        for selectionList in selectionPerm:

            answer = selectionList[0]

            for num in range(len(selectionList) - 1):
                if opList[num] == 'A':
                    answer = answer + selectionList[num + 1]
                if opList[num] == 'S':
                    answer = answer - selectionList[num + 1]
                if opList[num] == 'M':
                    answer = answer * selectionList[num + 1]
                if opList[num] == 'D':
                    if selectionList[num + 1] == 0:
                        break
                    else:
                        answer = answer / selectionList[num + 1]
            if answer == goal:
                winningNums.append(selectionList)
                winningOps.append(opList)

    if len(winningNums) == 0 and len(winningOps) == 0:
        print("THERE ARE NO RESULTS!")
    else:
        print("HERE ARE THE WINNING SOLUTIONS: ")
        opsDict = {
                    "A": " + ",
                    "S": " - ",
                    "M": " x ",
                    "D": " / "
                    }
        for x in range(len(winningNums)):
            winningEx = str(winningNums[x][0])
            for y in range(len(winningNums[x]) - 1):
                winningEx = winningEx + opsDict[winningOps[x][y]] + str(winningNums[x][y + 1]) + ','
            winningEx = winningEx + ' = ' + str(goal)
            print(winningEx)

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

        spaceLeft = spaces - len(smallArr) - len(largeArr)
        print("You have " + str(spaceLeft) + " numbers left!")

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
        
        spaceLeft = spaces - len(smallArr) - len(largeArr)
        print("You have " + str(spaceLeft) + " numbers left!")
    
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

    solveNumbersGame(goalNum, totalSelections)


    # Do a TIMER
    # Find the best algo to brute force the solution
        # https://stackoverflow.com/questions/48655612/find-all-numbers-that-sum-closest-to-a-given-number-python

def makeDict(length):
    f = open("words_alpha.txt","r")
    for word in f:
        word = word[:-1]
        if(len(word) <= length):
            word_dict.add(word)
    f.close()

def solveWordGame(dictionary, letters, solutions):
    letterPerm = list(permutations(letters))
    for perm in letterPerm:
        permWord = ""
        permWord = permWord.join(perm).lower()
        if permWord in dictionary:
            if permWord not in solutions:
                solutions.append(permWord)
                print("Found " + str(len(solutions)) + ' solutions so far!')

def lettersRound():
    print("It's time for a LETTERS ROUND")

    #default is 9 spaces
    spaces = 9

    print("You have " + str(spaces) + " spaces!")

    makeDict(spaces)

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

        spaceLeft = spaces - len(vowels) - len(consonants)
        print("You have " + str(spaceLeft) + " numbers left!")

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

        spaceLeft = spaces - len(vowels) - len(consonants)
        print("You have " + str(spaceLeft) + " numbers left!")

    totalSelections = consonants + vowels
    print("Your selections are...")
    print(totalSelections)

    print("Solving...")
    solutions = []
    letter_sets = list(chain.from_iterable(combinations(totalSelections, r) for r in range(1, len(totalSelections)+1)))
    for set in letter_sets:
        solveWordGame(word_dict, set, solutions)
    
    print(solutions)


def play():
    print("LET'S PLAY COUNTDOWN!")
    playing = True

    while playing:
        print("=====================")
        print("Choose from this menu: ")
        print("1: Numbers Round")
        print("2: Letters Round")
        print("3: Solve Letters Round")
        print("4: Solve Numbers Round")
        print("5: Quit")

        selection = input()

        if selection == '1':
            numbersRound()
        elif selection == '2':
            lettersRound()
        elif selection == '5':
            break
        else:
            print("Bad selection! Try again!")
            continue


play()