print('''
[1] - Transform raw score into z score
[2] - Transform z score into raw score
''')
choice = input('> ')
choice = int(choice)

def findzscore():
    mean = float(input('Enter the mean: '))
    standardD = float(input('Enter the standard deviation: '))
    rawscore = float(input('Enter the raw score: '))
    zscore = rawscore - mean
    zscore = zscore/standardD
    print('z score:', zscore)

def findrawfromz():
    mean = float(input('Enter the mean: '))
    standardD = float(input('Enter the standard deviation: '))
    zscore = float(input('Enter the z score: '))
    rawscore = zscore * standardD
    rawscore = rawscore + mean
    print('Raw score:', rawscore)
if choice == 1:
    findzscore()
elif choice == 2:
    findrawfromz()
else:
    next
