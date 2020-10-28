# Question Link: https://www.codewars.com/kata/54e6533c92449cc251001667

def unique_in_order(iterable):
    # compare successive elements using for loop
    return [i for idx,i in enumerate(iterable) if idx == 0 or i != iterable[idx-1]]

