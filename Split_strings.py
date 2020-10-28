# Question Link: https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

def solution(s):
    l = len(s)
    res = [s[i:i+2] for i in range(0,l,2)]
    if l%2 == 1:
        res[int(l/2)] = res[int(l/2)] + '_'
    return res