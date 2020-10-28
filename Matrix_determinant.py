# Question link: https://www.codewars.com/kata/52a382ee44408cea2500074c

def determinant(matrix):
#     If only one element, return it
    l = len(matrix)
    if l==1:
        return matrix[0][0]
#    Else, if the matrix is of size 2X2, return the determinant
    elif l==2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
#     Else, if the size is greater than 2X2, recursively call function itself and return the base case value. 
    elif l>2:
        res = 0
        mat = [[0 for col in range(l-1)] for row in range(l-1)]
        for i in range(l):
            r_row = [j for j in range(l) if j != 0]
            r_col = [j for j in range(l) if i != j]
            for k in range(l-1):
                for m in range(l-1):
                    mat[k][m] = matrix[r_row[k]][r_col[m]]
                    
            res = res + matrix[0][i]*determinant(mat)*((-1)**i)
        return res