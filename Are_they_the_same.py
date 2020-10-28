# Question Link: https://www.codewars.com/kata/550498447451fbbd7600041c

def comp(array1, array2):
    #Check if None
    if array1 is None or array2 is None:
        return False
    a1 = sorted([abs(i) for i in array1])
    a2 = sorted(array2)
    #Check if the sorted array of squares of a1 is same as sorted array a2 
    if len(a1) == len(a2) and a2 == [i**2 for i in a1]:
        return True
    else:
        return False
