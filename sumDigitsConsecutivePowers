#This program creates a range of a -> b and then does n ** 1, n+1 ** 1+1, n+2 ** 1+2, etc and if it equals the initial number it returns it 


def sum_dig_pow(a, b):
    digits = list(range(a, b+1))
    results = []
    for item in digits:
        if len(str(item)) == 1:
            results.append(item)
        else:
            num = [int(x) for x in str(item)]
            i = 0
            y = 0
            while i < len(num):
                y = y + (num[i] ** (i+1))
                i += 1
            if y == item:
                results.append(item)
    return results
    
    
    
##############
##Better Way##
##############

def filter_func(a):
    return sum(int(d) ** (i+1) for i, d in enumerate(str(a))) == a

def sum_dig_pow(a, b):
    return filter(filter_func, range(a, b+1)) ##The filter function tests if it something is true
