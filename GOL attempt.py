# game of life attempt start 30nov17

# make print '+' not '1'
# [make with colours (majority turns)]
# check for complete death
# do function for corners and then for sides - wrap around
# ^function for if i ==0, i=w-1 (and same for if i==w-1, -> i=0)

import csv, os
#with open('GOL1.csv', newline='') as golcsv:
 #   inputReader = csv.reader(golcsv)
  #  for row in inputReader:
   #     print(', '.join(row))

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def start():
    mycsv=input('Welcome! Please type the name of the input CSV file: ')
    
    MatrixA=initialize(mycsv)
    draw(MatrixA)
    while True:
        
        ask = input('\nDo you want to continue? Y/N\n')
        if ask.lower() == 'n':
            break
            # this is the end of the program
        elif ask.lower() == 'y':
            # next step
            os.system('cls')
            MatrixA = step(MatrixA)
            draw(MatrixA)
            # and false if all cells die...
        else:
            print('Incorrect input. Please try again.')
            continue
        
    
    
    
    

#create new separate function to initialise:
    #take in name of file to read and return variable
    


def initialize(inputFile):
    w, h = 20, 20;
    Matrix = [[0 for x in range(w)] for y in range(h)]

    
    
# WHAT IF WRONG TYPE OF FILE? THROW ERROR...

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


#def check(death):
    

def draw(Matrix):
    
    for i in range(len(Matrix)):
        print('\n', end=' ')
        for j in range(len(Matrix[i])):
            if Matrix[i][j] != 1:
                char = ' '
            else:
                char = '1'
            print(char, end=' ')
            
     # draw needs to just draw on screen, nothing else

def step(MatrixA):
    w = len(MatrixA)
    if w == 0:
        h=0
    else:
        h = len(MatrixA[0])
        
    MatrixB = [[0 for x in range(w)] for y in range(h)]

    for i in range(len(MatrixA)):
        
        for j in range(len(MatrixA[i])):

            if i == 0 or i == w-1 or j == 0 or j == h-1:
                MatrixB[i][j]=0
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


                
            




                        
                




            
            #thisCount = 0
            #for k in range(i-1, i+1):
                #if Matrix[k][j] == '1':
                        #thisCount += 1
                
                #for l in range(j-1, j+1):
                    
                    #if Matrix[i][l] == '1':
                        #thisCount += 1
            #print(thisCount, end=',')
               # if numberNeighbours != 0:
                #    print(numberNeighbours, end=',')
                        

    # if empty but has 3 neighbouring fulls, -> full.
    # if full and 2 or 3 neighbouring fulls, -> full.
    # if full and 1 or 0 or >3 neighbouring fulls, -> empty.

# make new matrix ; do step ; store new info from step in the new matrix.





start()
