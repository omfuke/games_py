import random

random.seed(30)


def Print(bo):
    for i in range(len(bo)):
        if i!=0 :
            print('-'*10)
        for j in range(len(bo)):
            print(bo[i][j], end='')
            if j %2 == 0 and j!=0:
                print('')
            else:
                print(' | ',end='')



def update(pos):
    if pos == 1:
        return (0,0)
    if pos == 2:
        return (0,1)
    if pos == 3:
        return (0,2)
    if pos == 4:
        return (1,0)
    if pos == 5:
        return (1,1)
    if pos == 6:
        return (1,2)
    if pos == 7:
        return (2,0)
    if pos == 8:
        return (2,1)
    if pos == 9:
        return (2,2)

def Valid(bo):
    if (bo[0][0] == bo[0][1]) and (bo[0][1] == bo[0][2]) and bo[0][0]!= '-':
        return True
    elif (bo[1][0] == bo[1][1]) and (bo[1][1] == bo[1][2]) and bo[1][0]!= '-':
        return True
    elif (bo[2][0] == bo[2][1]) and (bo[2][1] == bo[2][2]) and bo[2][0]!= '-':
        return True
    elif (bo[0][0] == bo[1][0]) and (bo[1][0] == bo[2][0]) and bo[2][0]!= '-':
        return True
    elif (bo[0][1] == bo[1][1]) and (bo[1][1] == bo[2][1]) and bo[2][1]!= '-':
        return True
    elif (bo[0][2] == bo[1][2]) and (bo[1][2] == bo[2][2]) and bo[2][2]!= '-':
        return True
    elif (bo[0][0] == bo[1][1]) and (bo[1][1] == bo[2][2]) and bo[2][2]!= '-':
        return True
    elif (bo[0][2] == bo[1][1]) and (bo[1][1] == bo[2][0]) and bo[2][0]!= '-':
        return True
    else:
        return None




def Game(bo,p1,p2):
    lis = [1,2,3,4,5,6,7,8,9]
    while True:
        if p1['chance'] == True:
            print('Player 1 ')
        else:
            print('Player 2 ')
        try:
            p = int(input('Enter position :'))
            if p in lis:
                lis.remove(p)
            else:
                print('Enter the Valid Position')
                continue
        except:
            print('Enter the Valid position')
            continue

        q = update(p)
        if p1['chance'] == True:
            bo[q[0]][q[1]] = p1['key']
            p1['chance'] = False
            p2['chance'] = True
        else:
            bo[q[0]][q[1]] = p2['key']
            p2['chance'] = False
            p1['chance'] = True
        if Valid(bo):
            if p1['chance'] == False:
                print('Winner is player 1')
                Print(bo)
                break
            else:
                print('Winner is player 2')
                Print(bo)
                break
        if not Valid(bo):
            if ('-' not in bo[0]) and ('-' not in bo[1]) and ('-' not in bo[2]):
                print('--------Game Tie---------')
                break

        Print(bo)





if __name__ == '__main__':
    board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]
    Print(board)

    bot1 = {'id': 1, 'key': 'M','chance':False}
    bot2 = {'id': 2, 'key': 'O','chance':False}
    turn = random.randint(1, 2)
    print('Its Player{}'.format(turn), 'chance')
    if bot1['id'] == turn:
        bot1['chance'] = True
    else:
        bot2['chance'] = True

    Game(board,bot1,bot2)