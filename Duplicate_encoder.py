# Question Link: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

def duplicate_encode(word):
    #your code here
    res = [')' if (word.lower()).count(i)>1 else '(' for i in word.lower()] # Create a new list of '(' or')' based on count of a particular character
    return "".join(res)