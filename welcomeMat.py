#Make a welcome mat, N should be an odd number and M should be N*3
def welcome_mat(N, M):
    middle = N//2+1
    for i in range(1, middle):
        center = (i*2-1)*".|."
        print(center.center(M,"-"))
        
    print("WELCOME".center(M,"-"))
    
    for i in reversed(range(1, middle)):
        center = (i*2-1)*".|."
        print(center.center(M,"-"))
        
    return


if __name__ == '__main__':
    #Take input N == rows, M == columns
    N, M = map(int, input().split(' '))
    
    welcome_mat(N, M)
