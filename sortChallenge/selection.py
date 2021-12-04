def findMin(arr):
    b = arr[0]
    for a in arr:
        if a < b:
            b = a
    final = arr.index(b)
    return final

def selection(arr):
    for a in range(len(arr) - 1):
        minvalue = findMin(arr[a : len(arr)]) + a
        arr[a], arr[minvalue] = arr[minvalue], arr[a]
    return arr

print(selection([6,5,10,3,1,4,8,2,9,7]))