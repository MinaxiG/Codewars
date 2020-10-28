# Question Link: https://www.codewars.com/kata/52bc74d4ac05d0945d00054e

def first_non_repeating_letter(string):
    '''Find char that have occured only once and return the first such char'''
    char = [string[(string.lower()).find(i)] for i in string.lower() if (string.lower()).count(i)<2]
    '''If no such char return "", else return the first char'''
    if len(char) == 0:
        return ""
    else:
        return char[0]