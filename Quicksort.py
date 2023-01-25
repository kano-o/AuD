arr = [2, 7, 5, 78, 9, 4]

def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q - 1)
        quicksort(array, q + 1, r)

def partition(array, p, r):
    x = array[r]
    i = p - 1

    for j in range(p, r - 1):
        if array[r] <= x:
            i = i +1
            swap = array[i]
            array[i] = array[j]
            array[j] = swap
    swap = array[i + 1]
    array[i +1] = array[r]
    array[r] = swap
    return i+1

print(quicksort(arr, arr[1], arr[len(arr)-1]))
