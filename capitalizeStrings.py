#If word starts with a number, return it as is. If it starts with a letter, capitalize the first letter

def solve(s):
    if s == "":
        return s
    words = s.split(" ")
    results = []
    for item in words:
        if item.isdigit():
            results.append(item)
        else:
            results.append(item.capitalize())
    return " ".join(results)

s = "hello world 12change"
print(solve(s))
