#program to retrun series 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 + ...
#pattern is add 3 to denominator
#Answer should be rounded to 2 decimals and returned as a str


def series_sum(n):
    if n == 0:
        return '{:.2f}'.format(n)
    elif n == 1:
        return '{:.2f}'.format(n)
    elif n == 2:
        return '{:.2f}'.format(1 + 1/4)
    result = 1 + 1/4
    while n > 2:
        result = result + (1/(4 +sum([3] * (n - 2))))
        n = n - 1
    return '{:.2f}'.format(result)


############
#Better Way#
############

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
