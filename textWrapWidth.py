#take a string and width and wrap the text based on that width

import textwrap

def wrap(string, max_width):
    wrapped = textwrap.wrap(string, max_width)
    result = '\n'.join(wrapped)
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
