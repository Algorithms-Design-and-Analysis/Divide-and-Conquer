# Paths in matrix (problem)
# Given a matrix where a cell has the value of 1 if it's a wall and 0 if not, find the number of ways to go from the top-left cell to the bottom-right cell, knowing that it's not possible to pass from a wall and we can only go to the right or to the bottom



# Example:

# input:
# matrix = [
#     [0, 0, 1, 0, 1],
#     [0, 0, 0, 0, 1],
#     [0, 0, 1, 0, 0],
#     [1, 0, 0, 0, 0]
# ]

# output: 7

def paths(matrix):
    
    filas = len(matrix)
    columnas = len(matrix[0])
    
    maneras = [[0]*columnas for i in range(filas)]
    
    maneras[0][0] = 1 if matrix[0][0] == 0 else 0
    
    for j in range(1, columnas):
        maneras[0][j] = 1 if maneras[0][j-1] == 1 and matrix[0][j] == 0 else 0
    
    for i in range(1, filas):
        maneras[i][0] = 1 if maneras[i-1][0] == 1 and matrix[i][0] == 0 else 0
        
    if matrix[0][0] == 1 or matrix[filas-1][columnas-1] == 1:
        return 0
    
    else:
        for i in range(1, filas):
            for j in range(1, columnas):
                 maneras[i][j] = maneras[i-1][j] +  maneras[i][j-1] if matrix[i][j] == 0 else 0
                 
    return maneras[filas-1][columnas-1]
                
        

