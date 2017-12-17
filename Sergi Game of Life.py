'''
Joseph Conway's Game of Life
Programmed by Sergi Bray
https://github.com/sergibot
Make input file in .csv format!
Easiest via Google Sheets:
create a 20x20 grid and place Game of Life 'seeds' by typing number '1' into cells.
File->Download as->comma-separated values (.csv)
Then move csv file into folder containing this program so we can access it here.
'''
import csv, os
# The main function of our program - other functions are called within this.
def start():
    # We ask the user to point the program to a CSV (comma-separated variable) file.
    # This file should be saved in the same folder as the program is in, and
    # the user will have to enter the full file name, including '.csv'.
    mycsv=input('Welcome! Please type the name of the input CSV file: ')
    # The initialize function puts the selected .csv file into
    # matrix form and we pass that into MatrixA, draw function
    # then prints this initial matrix as grid of cells.
    MatrixA=initialize(mycsv)
    draw(MatrixA)
    while True:
        # After each step, ask user to continue or stop the program.
        ask = input('\nDo you want to continue? Y/N\n')
        # If user stops the program, break. This is one end to the program.
        if ask.lower() == 'n':
            break
        # If continue, carry onto the next step (refreshing screen and grid).
        elif ask.lower() == 'y':
            os.system('cls')
            MatrixB = step(MatrixA)
            draw(MatrixB)
            # Check if matrix identical to previous matrix, if yes then
            # this is because all cells dead or pattern stuck on repeat.
            # If either is so, grid will recur forever, so stop program here.
            if compare(MatrixA,MatrixB):
                print('\n\nThe cells will live on in this state forever.')
                print('Game Over.')
                break
            # If matrices at all dissimilar, continue program. 
            else:
                MatrixA = MatrixB
        # Need to catch incorrect input.
        else:
            print('Incorrect input. Please try again.')
# Converts .csv file into matrix our program can use (w is width,
# h is height of grid/matrix, can be redefined for bigger grids).
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
# Draw grid with '+' symbols representing cell life (' ' = dead cell).
def draw(Matrix):    
    for i in range(len(Matrix)):
        print('\n', end=' ')
        for j in range(len(Matrix[i])):
            if Matrix[i][j] != 1:
                char = ' '
            else:
                char = '+'
            print(char, end=' ')
# cls function will refresh the screen so program can redraw grid
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
# Depending on total living neighbours determine cell life next turn.
def step(MatrixA):
    w = len(MatrixA)
    h = len(MatrixA[0])        
    MatrixB = [[0 for x in range(w)] for y in range(h)]
    # Fill new matrix with cells live/dead depending on last matrix.
    for i in range(len(MatrixA)):        
        for j in range(len(MatrixA[i])):
            # Add w/h so modulo works for top and left sides.
            x = w + i 
            y = h + j             
            A = MatrixA[(x-1)%w][(y-1)%h]
            B = MatrixA[(x)%w][(y-1)%h]
            C = MatrixA[(x+1)%w][(y-1)%h]
            D = MatrixA[(x-1)%w][(y)%h]
            E = MatrixA[(x)%w][(y)%h] 
            F = MatrixA[(x+1)%w][(y)%h]
            G = MatrixA[(x-1)%w][(y+1)%h]
            H = MatrixA[(x)%w][(y+1)%h]
            I = MatrixA[(x+1)%w][(y+1)%h]
            # Calculate total neighbours and next turn death/life
            total=A+B+C+D+F+G+H+I
            if E == 0 and total == 3:
                MatrixB[i][j]=1
            elif E == 1 and (total == 2 or total ==3):
                MatrixB[i][j]=1
            elif E == 1 and total == 0 or total ==1:
                MatrixB[i][j]=0
            elif E == 1 and total > 3:
                MatrixB[i][j]=0                
    return MatrixB
# Check whether new matrix is identical to last turn's matrix.
def compare(MatrixA,MatrixB):
    allSame = True        
    for i in range(len(MatrixA)):        
        for j in range(len(MatrixA[i])):
            if MatrixA[i][j] != MatrixB[i][j]:
                allSame = False
                break
    return allSame            
start()
