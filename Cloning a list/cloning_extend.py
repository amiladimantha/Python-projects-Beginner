list = [1, 6, 3, 5, 3, 4 ]

li_copy = []
def clone(l):
    li_copy.extend(l)
    return li_copy
    
print("Before: ", li_copy)
print("After: ", clone(list))