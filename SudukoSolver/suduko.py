board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# Print Board
def Print(bo):

    for i in range(len(bo)):
        if i%3 == 0 and i!=0:
            print('- '*11)
        for j in range(len(bo)):
            if j%3 == 0 and j!=0:
                print('|',end=' ')
            if j==8:
                print(bo[i][j])
                break

            print(bo[i][j],end=' ')

#Printing  Board Done


# Empty with Position
def get_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j] == 0:
                return (i,j)
    return None


zeros = get_empty(board)
print(zeros)


# validity check

def valid(bo,num,pos):
    #x_valid
    for i in range(len(board)):
        if bo[pos[0]][i]==num and pos[1]!=i:
            return False

    #y_valid
    for i in range(len(board)):
        if bo[i][pos[1]]== num and pos[0]!= i :
            return False

    #box_valid
    x = pos[0]//3
    y = pos[1]//3

    for i in range(x*3,x*3+3):
        for j in range(y*3,y*3+3):
            if bo[i][j] == num and pos !=(i,j):
                return False

    return True


#Solve


def solve(bo):

    find = get_empty(bo)
    if not find:
        return True

    else:

        row,col = get_empty(bo)

    for i in range(1,10):

        if valid(bo,i,(row,col)):
            bo[row][col] = i


            if solve(bo):
                return True

            bo[row][col] = 0

    return False



solve(board)
Print(board)