#1 to n inlcusive
#if i is a multiple of 3 and 5 print FizzBuzz
#if i is a multiple of 3, but not 5, print Fizz
#if i is a multiple of 5, but not 3, print Buzz 
#if i is not a multiple of 5 or 3, print i


def fizzBuzz(n):
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            print(i,"FizzBuzz")
        elif i % 3 == 0:
            print(i,"Fizz")
        elif i % 5 == 0:
            print(i,"Buzz")
        else:
            print(i)
        i += 1

fizzBuzz(5)
