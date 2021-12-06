#string validators
#.isalnum() will check if the string is alphanumeric
#.isalpha() will check if the string is alphabetical
#.isdigit() will check if the string is numeric 
#.islower() will check if the string is lowercase
#.isupper() will check if the string is uppercase

if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    
    for item in s:
        if item.isalnum() == True:
            alnum = True
        if item.isalpha() == True:
            alpha = True
        if item.isdigit() == True:
            digit = True
        if item.islower() == True:
            lower =  True
        if item.isupper() == True:
            upper = True
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
    
################
    
s = input()
print(any(c.isalnum()  for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))

########

s = input()
for test in ('isa'islnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
    print(any(eval("c." + test + "()") for c in s))
