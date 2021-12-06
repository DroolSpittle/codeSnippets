#Enter the number of commands and then enter what to do with the list
#Consider a list (list = []). You can perform the following commands:

#insert i e: Insert integer  at position .
#print: Print the list.
#remove e: Delete the first occurrence of integer .
#append e: Insert integer  at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list.

if __name__ == "__main__":
    intList = []
    for _ in range(int(input())):
        command = input()
        commandList = command.split()
        if commandList[0] == "insert":
            intList.insert(int(commandList[1]), int(commandList[2]))
        elif commandList[0] == "print":
            print(intList)
        elif commandList[0] == "remove":
            intList.remove(int(commandList[1]))
        elif commandList[0] == "append":
            intList.append(int(commandList[1]))
        elif commandList[0] == "sort":
            intList.sort()
        elif commandList[0] == "pop":
            intList.pop()
        elif commandList[0] == "reverse":
            intList.reverse()
    
