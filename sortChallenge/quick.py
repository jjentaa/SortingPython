def qs(arr):
    less = []
    equal = []
    more = []
    if len(arr) > 1:
        pivot = arr[0]
        
        for i in range(len(arr)):
            if arr[i] > pivot:
                more.append(arr[i])
            elif arr[i] < pivot:
                less.append(arr[i])
            else:
                equal.append(arr[i])
        
        return qs(less)+equal+qs(more)
    else:
        return arr

print(qs([6,5,10,3,1,4,8,2,9]))