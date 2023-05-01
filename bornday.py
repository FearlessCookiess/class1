user = int(input('please enter birthday year of writer A.S.Pushkin: '))

if user == 1799:
    print('you are right')
    day = int(input('please enter day of birthday A.S.Pushkin: '))
    if day == 6:
        print('you have a good knowledge about A.S.Pushkin')
    elif day <= 6 or day >= 6:
     print('day it wrong try one more time')
else:
    print('you are wrong, try again')



