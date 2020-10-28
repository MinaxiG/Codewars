# Question Link: https://www.codewars.com/kata/52f787eb172a8b4ae1000a34

import math
def zeros(n):
    return sum([n//(5**i) for i in range(1,math.ceil(math.log(n+1,5))) if n//(5**i)>0])