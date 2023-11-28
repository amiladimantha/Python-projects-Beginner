def swap(newList):
    first = newList[0]
    newList[0] = newList[-1]
    newList[-1] = first
    
    return newList


newList = [12, 35, 9, 56, 24]
print(swap(newList))