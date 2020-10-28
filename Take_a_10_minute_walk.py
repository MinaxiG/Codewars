# Question Link: https://www.codewars.com/kata/54da539698b8a2ad76000228

def is_valid_walk(walk):
    #If walk is valid total number of letters would be 10 and numbers of 'n' and 's' will be equal and so as numbers of 'w' and 'e'
    return walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e') and len(walk)==10
