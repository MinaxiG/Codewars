# Question Link: https://www.codewars.com/kata/514a024011ea4fb54200004b

def domain_name(url):
    idx = [idx for idx, i in enumerate(url) if i == '.']
    #Select subtsrings based on following conditions:
    if url.find('www')>-1: 
        return url[idx[0]+1:idx[1]]
    elif url.find('//')>-1:
        return url[url.find('/')+2:url.find('.')]
    else:
        return url[0:url.find('.')]