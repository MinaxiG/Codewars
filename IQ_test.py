# Question Link: https://www.codewars.com/kata/552c028c030765286c00007d

def iq_test(numbers):
    #your code here
    l = numbers.split(" ")                   # Split the text into list of elements
    num = [int(i) for i in l if i != ' ']    # Convert the string elements to integers
    even = [i for i in num if i%2==0]        # Separate out all the even integers
    if len(even) == 1:                       # If only one even element, return it's index
        return num.index(even[0])+1
    else:                                    # If only one odd element, return it's index
        odd = [i for i in num if i not in even]
        return num.index(odd[0])+1