# Question Link: https://www.codewars.com/kata/545cedaa9943f7fe7b000048

import string

def is_pangram(s):
    small = [chr(i) for i in range(ord('a'), ord('z')+1)]  #list of all alphabets
    [small.remove(i) for i in s.lower() if i in small]     #removes the occured alphabet
    res = len(small)
    if res == 0:
        return True
    else:
        return False