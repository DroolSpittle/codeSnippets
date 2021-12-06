#given an input of n ints, print the hash of the tuple t for which t = integer_list

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
