#for x,y,z being dimensions of a cuboid in a 3d grid, output all the combinations where x+y+z != n


def cuboid(x, y, z, n):
    permutations = []
    xlist = [ i for i in range(x+1) ]
    ylist = [ i for i in range(y+1) ]
    zlist = [ i for i in range(z+1) ]
    permutations = [[xitem, yitem, zitem] for xitem in xlist for yitem in ylist for zitem in zlist]

    for item in permutations[:]:
        if sum(item) == n:
            permutations.remove(item)
    
    
    return permutations
    
    
    
    
x = 1
y = 1 
z = 1
n = 2

print(cuboid(x, y, z, n))
