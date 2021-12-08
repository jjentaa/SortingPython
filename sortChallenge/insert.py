def insert(arr):
    for a in range(len(arr)):
        e = a
        for b in range(a, -1, -1):
            if arr[e] < arr[b]:
                arr[e], arr[b] = arr[b], arr[e]
                e -= 1
    return arr

print(insert([6,5,10,3,1,4,8,2,9,7]))