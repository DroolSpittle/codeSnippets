def expanded_form(num):
    zeros = len(str(num))
    result =''
    i = 0 
    while i < len(str(num)):
        result += (str(num)[i].ljust(zeros, "0"))
        result += ';'
        i += 1
        zeros -= 1
    result = result.split(';')
    result.remove('')
    result = [x for x in result if int(x) != 0]
    return ' + '.join(result)
    
    ##################
    ####Better Way####
    ##################
    
def expanded_form(num):
  num = list(str(num))
  return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')
