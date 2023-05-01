user = int(input('write year of birthday A.S.Pushkin: '))
while user != 1799:
    print('you are wrong')
    user = int(input('write year of birthday A.S.Pushkin: '))
if user == 1799:
    user = int(input('write day of birthday A.S.Pushkin: '))
while user != 6:
    user = int(input('write day of birthday A.S.Pushkin: '))

else:
    print('you are right')
