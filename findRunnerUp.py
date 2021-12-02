#Given participants score sheet for sports day, you are required to find the runner up. n is the runner up score, A is the list of scores

def findRunnerUp(n, A):
    scores = []
    for i in A:
        if i not in scores:
            scores.append(i)
    n = len(scores)
    for i in range(n):
        for j in range(n - i -1):
            if scores[j] > scores[j + 1]:
                scores[j], scores[j + 1] = scores[j + 1], scores[j]
    runnerUp = scores[-2]
    return runnerUp
    


scores = [2,3,6,6,5]
print(findRunnerUp(5, scores))


##############
##Better Way##
##############

#Given participants score sheet for sports day, you are required to find the runner up. n is the runner up score, A is the list of scores

def findRunnerUp(n, A):
    scores = []
    for i in A:
        if i not in scores:
            scores.append(i)
    scores.sort()
    #.sort() will sort the list sorted(scores) would be used to create a new list without affecting the list
    runnerUp = scores[-2]
    return runnerUp
    


scores = [2,3,6,6,5]
print(findRunnerUp(5, scores))
