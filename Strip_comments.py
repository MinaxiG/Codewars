# Question Link: https://www.codewars.com/kata/51c8e37cee245da6b40000bd

def solution(string,markers):
    '''Split the string based on newlines'''
    diff = string.split('\n')
    res = []          #Final result variable
    '''If each line contains any markers, append only the initial part of the line else append the whole line'''
    for i in diff:
        j = sorted([i.find(j) for j in markers if i.find(j)>-1])
        if len(j)>0:
            res.append((i[0:j[0]]).strip())
        else:
            res.append(i.strip())
            
    return "\n".join(res)  # Join all the separate with '\n' to bring back to original format 