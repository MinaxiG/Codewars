# Question Link: https://www.codewars.com/kata/53dbd5315a3c69eed20002dd

def filter_list(l):
    nl = []
    [nl.append(i) for i in l if isinstance(i, int)]      
    return nl