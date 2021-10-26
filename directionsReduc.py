def dirReduc(arr):
    result = arr
    changes = 0
    i = 0
    while i < len(arr) - 1:
        if arr[i] == 'NORTH' and arr[i+1] == 'SOUTH':
            result.remove('NORTH')
            result.remove('SOUTH')
            changes += 1
            if len(result) == 1:
                break
        if arr[i] == 'SOUTH' and arr[i+1] == 'NORTH':
            result.remove('SOUTH')
            result.remove('NORTH')
            changes += 1
            if len(result) == 1:
                break
        if arr[i] == 'EAST' and arr[i+1] == 'WEST':
            result.remove('EAST')
            result.remove('WEST')
            changes += 1
            if len(result) == 1:
                break
        if arr[i] == 'WEST' and arr[i+1] == 'EAST':
            result.remove('WEST')
            result.remove('EAST')
            changes += 1
            if len(result) == 1:
                break
        i += 1
    if changes > 0:
        return (dirReduc(result))
    else:
        return result
