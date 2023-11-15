import random
import string

def numbersRound():
    print("It's time for a NUMBERS ROUND!")
    spaces = 6
    possibleLarge = [50, 25, 10, 75, 100]

    smallArr = []
    largeArr = []
    
    while(len(smallArr) + len(largeArr) < 6):
        # Get num Small numbers
        while(True):
            print('How many small numbers would you like?')
            numSmall = input()
            print('You picked ' + numSmall + ' small numbers!')
            numSmall = int(numSmall)

            if(numSmall > 6 or len(smallArr) + len(largeArr) + numSmall > 6):
                print('Too many! Try again')
                continue
            else:
                break

        # For loop to select
        for x in range(int(numSmall)):
            randomSmall = random.randint(0, 10)
            smallArr.append(randomSmall)
        
        # Check to see if it is done (all spaces filled)
        if(len(smallArr) + len(largeArr) >=6 ):
            break

        # Get num Large numbers
        while(True):
            print('How many large numbers would you like?')
            numLarge = input()
            print('You picked ' + numLarge + ' large numbers!')
            numLarge = int(numLarge)

            if(numLarge > 6 or len(smallArr) + len(largeArr) + numLarge > 6):
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
    


    #OR... work on letters round using ASCII
def lettersRound():
    print('LET')
    spaces = 9
    string.ascii_letters
    print(random.choice(string.ascii_uppercase))


def play():
    print('PlayTime')
    #numbersRound()
    lettersRound()


play()