# Question Link: https://www.codewars.com/kata/546f922b54af40e1e90001da

def alphabet_position(text):
#     Create a list of all the alphabets wheather small or capitals
    small = [chr(i) for i in range(ord('a'), ord('z')+1)]
    big = [chr(i) for i in range(ord('A'), ord('Z')+1)]

    res = ""                #     Initialise a string
    for i in text:
        if i in small:
            res = res + str(small.index(i)+1) + " "    #concatenate the index for each small alphabet with a space
        elif i in big:
            res = res + str(big.index(i)+1) + " "      #concatenate the index for each big alphabet with a space
        else:
            pass
        
    return res[:-1]       #remove space at the end
