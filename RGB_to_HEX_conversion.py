# Question Link: https://www.codewars.com/kata/513e08acc600c94f01000001

def rgb(r, g, b):
    rgb = [r,g,b]
    rgb = [0 if i<0 else i for i in rgb]
    rgb = [255 if i>255 else i for i in rgb]
    return ((hex(rgb[0])[-2:]+hex(rgb[1])[-2:]+hex(rgb[2])[-2:]).upper()).replace('X', '0') #Convert decimal to hexadecimal values