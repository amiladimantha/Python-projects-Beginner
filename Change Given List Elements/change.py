def swap(newList, a, b):
    first = newList[a]
    newList[a] = newList[b]
    newList[b] = first
    
    return newList



newList = [12, 35, 9, 56, 24]
print(swap(newList,2,3))