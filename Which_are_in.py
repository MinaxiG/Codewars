# Question Link: https://www.codewars.com/kata/550554fd08b86f84fe000a58

def in_array(array1, array2):
    # Using nested for loop in list comprehension, make a list of substring, remove duplicates and then sort. 
    return sorted(list(dict.fromkeys([i for i in array1 for j in array2 if j.find(i)>-1])))