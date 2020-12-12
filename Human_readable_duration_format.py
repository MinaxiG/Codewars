#Link to Question: https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_duration(seconds):
    #your code here
    s = seconds
    y = seconds//60//60//24//365                      # no. of years
    d = (s-y*60*60*24*365)//60//60//24                # no. of days
    h = (s-y*60*60*24*365-d*60*60*24)//60//60         # no. of hours    
    m = (s-y*60*60*24*365-d*60*60*24-h*3600)//60      # no. of minutes
    ss = (s-y*60*60*24*365-d*60*60*24-h*3600-m*60)    # no. of seconds
    
    a = [y, d, h, m, ss]
    s = ['year', 'day', 'hour', 'minute', 'second']
    p = ['years', 'days', 'hours', 'minutes', 'seconds']
    
    r = [idx for idx,i in enumerate(a) if i>=1]
    res = ["{}".format(str(a[idx]))+' '+p[idx] if a[idx]>1 else "{}".format(str(a[idx]))+' '+s[idx] for idx in r]
    if len(res) == 0:
        return 'now'    
    if len(res)==1:
        return '{}'.format(''.join(res))
    else:
        l = len(res)
        res[l-2] = res[l-2]+' and '+res[l-1]
        res.pop()
        return '{}'.format(', '.join(res))
