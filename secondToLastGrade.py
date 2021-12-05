#Find the student(s) with the second to lowest grade

def findSecondToLowest(grades):
    res = sorted(grades, key = lambda x: x[1])
    secondToLast = []
    scores = []
    for item in res:
        if item[1] not in scores:
            scores.append(item[1])
    for item in res:
        if item[1] == scores[1]:
            secondToLast.append(item[0])
    secondToLast.sort()
    print(*secondToLast, sep = "\n")
    return

if __name__ == '__main__':
    grades = []
#    for _ in range(int(input())):
#        name = input()
#        score = float(input())
#        grades.append([name, score])

    grades = [["Harry", 20], ["Berry", 20], ["Tina", 19], ["Akriti", 19], ["Harse", 21], ["Charles", 21]]
    findSecondToLowest(grades)
