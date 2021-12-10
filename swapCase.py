def swap_case(s):
    result = ""
    for char in s:
        if char.isupper() == False:
            result = result + char.upper()
        if char.isupper() == True:
            result = result + char.lower()
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
