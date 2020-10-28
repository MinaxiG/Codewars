# Question Link: https://www.codewars.com/kata/52685f7382004e774f0001f7

def make_readable(seconds):
    # Do something
    HH = int(seconds/3600)                 #Calculate no. of hours
    MM = int((seconds-HH*3600)/60)         #Calculate no. of minutes
    SS = seconds-HH*3600-MM*60             #Calculate no. of seconds
    return "{}:{}:{}".format('0'+str(HH) if HH<10 else HH, '0'+str(MM) if MM<10 else MM, '0'+str(SS) if SS<10 else SS)
    
