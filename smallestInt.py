def find_smallest_int(arr):
    smallest = arr[0]
    i = 0
    while i < len(arr) - 1:
        if smallest > arr[i+1]:
            smallest = arr[i+1]
        i = i + 1
    return smallest
