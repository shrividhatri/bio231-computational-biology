'''
POSSIBLE ALLIGNMENTS FROM SEQUENCE LENGTHS - PYTHON

Write a programme that takes two sequence lengths as input
and outputs the number of possible alignments between them on the screen.

m = sequence 1 length
n = sequence 2 length
minimum alignment length = max(m,n) length of bigger sequence
maximum alignment length = m*n
'''

'''
count number of routes to reach matrix node position (i, j) by only
being restricted to only vertical, horizontal or diagonal movement
starting from the first left-top-most node (0,0)

i,j counters - initialised manually to starting position 0,0 for left-top-most node
endi, endj - endpoint node's position coordinates 
'''
def numRoutesDNPMatrix(i, j, endi, endj):
    #  base case, stopping condition - row index is first, or column index is the first
    if (i == endi or j == endj):  #  when the index reaches border conditions bottom-right-most, right-most, bottom-most
        return 1

    #  traverse vertically, horizontally and diagonally recursively
    return numRoutesDNPMatrix(i+1, j, endi, endj) + numRoutesDNPMatrix(i, j+1, endi, endj) + numRoutesDNPMatrix(i+1, j+1, endi, endj)
    

retry = 'r'
while(retry == 'r'):
    m = int(input("Length of first sequence: "))
    n = int(input("Length of second sequence: "))

    '''
    imagine creating a DNP matrix of dimensions m+1 * n+1 for
    the two sequences and tracing all routes through it, starting from position
    # (0,0) to every other position in the matrix (1,1, 2,1, 2,3,... m+1,n+1) so up to (m+1, n+1)
    '''
    answer = 0
    '''
    for x in range(2, m+1):
         for y in range(2, n+1):
             answer += numRoutesDNPMatrix(1, 1, x, y)
    '''
    answer = numRoutesDNPMatrix(1, 1, m+1, n+1)
    print("The number of possible alignments between the two sequences is: %i" % answer)
    retry = input('Enter \'r\' to do another search, any other key to terminate the program: ') # retry input
    print('\n')
