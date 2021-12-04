def bbs(arr):
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    
    return arr

print(bbs([6,5,10,3,1,4,8,2,9,7]))