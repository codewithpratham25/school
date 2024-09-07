import random

comp = random.choice([1,2,3])
time = int(input("Enter the number of times you want to play: "))
compPoints = 0
youPoints = 0
for i in range(time):
    youstr = input("Enter your choice(s --> Stone, p --> Paper, sc --> Sciscors): ")
    if youstr == 's' or youstr == 'S' or youstr == 'P' or youstr == 'p' or youstr == 'SC' or youstr == 'sc' or youstr == 'sC' or youstr == 'Sc':
        pass
    else:
        print('Error: Wrong Input')
        exit()
    youDIct = {'s': 1,'p':2,'sc':3}
    reverseDict = {1:'Stone',2:'Paper',3:'Sciscors'}

    you = youDIct[youstr]
    print(f'You selected {reverseDict[you]} and computer selected {reverseDict[comp]}')
    if comp == you:
        print("Its a Draw")
    else:
        if comp == 1 and you == 2:
            print('You Win')
            youPoints += 1
            print(f'Points:\n Computer Points --> {compPoints}\n Your Points --> {youPoints}')
        elif comp == 1 and you == 3:
            print('You Lost')
            compPoints += 1
            print(f'Points:\n Computer Points --> {compPoints}\n Your Points --> {youPoints}')
        elif comp == 2 and you == 1:
            print('You Lost')
            compPoints += 1
            print(f'Points:\n Computer Points --> {compPoints}\n Your Points --> {youPoints}')
        elif comp == 3 and you == 1:
            print('You Win')
            youPoints += 1
            print(f'Points:\n Computer Points --> {compPoints}\n Your Points --> {youPoints}')
        elif comp == 2 and you == 3:
            print('You Win')
            youPoints += 1
            print(f'Points:\n Computer Points --> {compPoints}\n Your Points --> {youPoints}')
        elif comp == 3 and you == 2:
            print('You Lost')
            compPoints += 1
            print(f'Points:\n Computer Points --> {compPoints}\n Your Points --> {youPoints}')
        else:
            print("Something went wrong")
if compPoints > youPoints:
    print('Computer Won!')
else:
    print('You Won!')