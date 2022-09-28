import random
from re import L

def list():
    LIST = []
    for i in range(30):
        LIST.append(random.randint(0,9))
    return LIST

'''
search and sort
'''
def l_search(arr: list, target: int):
    # liniar search


    for i in range(len(arr)):
        if target == arr[i]:
            return i
# print(l_search([1, 2,3 ,4 ,5], 4))





'''
Binary search, complete two pointers and divide sorted array in half, check which target is in and repeat as expected
'''
def b_search(arr: list, start: int, end: int, target:int):
    arr.sort()
    n = 1
    print(arr)
    if target not in arr:
        return "no target found"
    while start <= end:
        
        print(n)
        n += 1
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid +1 

        elif arr[mid] > target:
            end = mid - 1
        
        else:
            return mid
# print(b_search(arr = list(), start = 0, end = 9, target = 7))
    
