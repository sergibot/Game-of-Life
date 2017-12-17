# game of life attempt start 30nov17

import csv, os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def start():
    mycsv=input('Welcome! Please type the name of the input CSV file: ')
    
    MatrixA=initialize(mycsv)
    draw(MatrixA)
    while True:
        
        ask = input('\nDo you want to continue? Y/N\n')
        if ask.lower() == 'n':
            # This calls an end to the program from user input.            
            break
        # If user tells program to continue, proceed through next step.
        elif ask.lower() == 'y':
            os.system('cls')
            MatrixB = step(MatrixA)
            draw(MatrixB)
            # The compare function returns True if all cells same.
            # We use this to stop the program when matrices recur.
            if compare(MatrixA,MatrixB):
                # This calls an end to the program if the matrices recur
                # (because they will recur infinitely and look the same).                
                print('\n\nThe cells will live on in this state forever.')
                print('Game Over.')
                break
            else:
                MatrixA = MatrixB # continues the program
        else:
            print('Incorrect input. Please try again.')

def initialize(inputFile):
    w, h = 20, 20;
    Matrix = [[0 for x in range(w)] for y in range(h)]

    with open(inputFile, newline='') as golcsv:
        inputReader = csv.reader(golcsv)
        i=0
        for row in inputReader:            
            for j in range(len(row)):
                temp=row[j]
                if temp == '1':
                    Matrix[i][j] = 1
                else:
                    Matrix[i][j] = 0            
            i+=1                    
    return Matrix

def draw(Matrix):    
    for i in range(len(Matrix)):
        print('\n', end=' ')
        for j in range(len(Matrix[i])):
            if Matrix[i][j] != 1:
                char = ' '
            else:
                char = '+'
            print(char, end=' ')            

def step(MatrixA):
    w = len(MatrixA)
    if w == 0:
        h=0
    else:
        h = len(MatrixA[0])        
    MatrixB = [[0 for x in range(w)] for y in range(h)]
    for i in range(len(MatrixA)):        
        for j in range(len(MatrixA[i])):
            if False:
                MatrixB[i][j]=0
            else:
                # top left 
                if i == 0 and j == 0:
                    A = MatrixA[w-1][h-1]
                    B = MatrixA[i][h-1]
                    C = MatrixA[i+1][h-1]
                    D = MatrixA[w-1][j]
                    G = MatrixA[w-1][j+1]
                    
                    #A = MatrixA[i-1][j-1]
                    #B = MatrixA[i][j-1]
                    #C = MatrixA[i+1][j-1]
                    #D = MatrixA[i-1][j]
                    E = MatrixA[i][j]
                    F = MatrixA[i+1][j]
                    #G = MatrixA[i-1][j+1]
                    H = MatrixA[i][j+1]
                    I = MatrixA[i+1][j+1]    

                # top right
                elif i == 0 and j == h-1:
                    A = MatrixA[w-1][j-1]
                    D = MatrixA[w-1][j]
                    G = MatrixA[w-1][h-1]
                    H = MatrixA[i][h-1]
                    I = MatrixA[i+1][h-1]

                    #A = MatrixA[i-1][j-1]
                    B = MatrixA[i][j-1]
                    C = MatrixA[i+1][j-1]
                    #D = MatrixA[i-1][j]
                    E = MatrixA[i][j]
                    F = MatrixA[i+1][j]
                    #G = MatrixA[i-1][j+1]
                    #H = MatrixA[i][j+1]
                    #I = MatrixA[i+1][j+1]

                # bottom right
                elif i == w-1 and j == h-1:
                    C = MatrixA[0][j-1]
                    F = MatrixA[0][j]
                    G = MatrixA[i-1][0]
                    H = MatrixA[i][0]
                    I = MatrixA[0][0]

                    A = MatrixA[i-1][j-1]
                    B = MatrixA[i][j-1]
                    #C = MatrixA[i+1][j-1]
                    D = MatrixA[i-1][j]
                    E = MatrixA[i][j]
                    #F = MatrixA[i+1][j]
                    #G = MatrixA[i-1][j+1]
                    #H = MatrixA[i][j+1]
                    #I = MatrixA[i+1][j+1]

                # bottom left
                elif i == w-1 and j == 0:
                    A = MatrixA[i-1][h-1]
                    B = MatrixA[i][h-1]
                    C = MatrixA[0][h-1]
                    F = MatrixA[0][j]
                    I = MatrixA[0][j+1]

                    #A = MatrixA[i-1][j-1]
                    #B = MatrixA[i][j-1]
                    #C = MatrixA[i+1][j-1]
                    D = MatrixA[i-1][j]
                    E = MatrixA[i][j]
                    #F = MatrixA[i+1][j]
                    G = MatrixA[i-1][j+1]
                    H = MatrixA[i][j+1]
                    #I = MatrixA[i+1][j+1]
                    
                # left edge (we've accounted for corners)
                elif i == 0:
                    A = MatrixA[w-1][j-1]
                    D = MatrixA[w-1][j]
                    G = MatrixA[w-1][j+1]

                    #A = MatrixA[i-1][j-1]
                    B = MatrixA[i][j-1]
                    C = MatrixA[i+1][j-1]
                    #D = MatrixA[i-1][j]
                    E = MatrixA[i][j]
                    F = MatrixA[i+1][j]
                    #G = MatrixA[i-1][j+1]
                    H = MatrixA[i][j+1]
                    I = MatrixA[i+1][j+1]

                # right edge
                elif i == w-1:
                    C = MatrixA[0][j-1]
                    F = MatrixA[0][j]
                    I = MatrixA[0][j+1]

                    A = MatrixA[i-1][j-1]
                    B = MatrixA[i][j-1]
                    #C = MatrixA[i+1][j-1]
                    D = MatrixA[i-1][j]
                    E = MatrixA[i][j]
                    #F = MatrixA[i+1][j]
                    G = MatrixA[i-1][j+1]
                    H = MatrixA[i][j+1]
                    #I = MatrixA[i+1][j+1]

                # top edge
                elif j == 0:
                    A = MatrixA[i-1][h-1]
                    B = MatrixA[i][h-1]
                    C = MatrixA[i+1][h-1]

                    #A = MatrixA[i-1][j-1]
                    #B = MatrixA[i][j-1]
                    #C = MatrixA[i+1][j-1]
                    D = MatrixA[i-1][j]
                    E = MatrixA[i][j]
                    F = MatrixA[i+1][j]
                    G = MatrixA[i-1][j+1]
                    H = MatrixA[i][j+1]
                    I = MatrixA[i+1][j+1]

                # bottom edge
                elif j == h-1:
                    G = MatrixA[i-1][0]
                    H = MatrixA[i][0]
                    I = MatrixA[i+1][0]

                    A = MatrixA[i-1][j-1]
                    B = MatrixA[i][j-1]
                    C = MatrixA[i+1][j-1]
                    D = MatrixA[i-1][j]
                    E = MatrixA[i][j]
                    F = MatrixA[i+1][j]
                    #G = MatrixA[i-1][j+1]
                    #H = MatrixA[i][j+1]
                    #I = MatrixA[i+1][j+1]

                else:                    
                    A = MatrixA[i-1][j-1]
                    B = MatrixA[i][j-1]
                    C = MatrixA[i+1][j-1]
                    D = MatrixA[i-1][j]
                    E = MatrixA[i][j]
                    F = MatrixA[i+1][j]
                    G = MatrixA[i-1][j+1]
                    H = MatrixA[i][j+1]
                    I = MatrixA[i+1][j+1]
                # calculate the total neighbours of each selected cell
                total=A+B+C+D+F+G+H+I
                # the cell lives or dies according to the rules of the game
                if E == 0 and total == 3:
                    MatrixB[i][j]=1
                elif E == 1 and (total == 2 or total ==3):
                    MatrixB[i][j]=1
                elif E == 1 and total == 0 or total ==1:
                    MatrixB[i][j]=0
                elif E == 1 and total > 3:
                    MatrixB[i][j]=0                                
    return MatrixB                            

def compare(MatrixA,MatrixB):

    allSame = True    
    for i in range(len(MatrixA)):        
        for j in range(len(MatrixA[i])):
            if MatrixA[i][j] != MatrixB[i][j]:
                allSame = False
                break
    return allSame            


start()
