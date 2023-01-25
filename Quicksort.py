

def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q - 1)
        quicksort(array, q + 1, r)

def partition(array, p, r):
    x = array[r]
    i = p - 1

    for j in range(p, r):
        if array[j] <= x:
            i = i +1
            swap = array[i]
            array[i] = array[j]
            array[j] = swap
    swap = array[i + 1]
    array[i +1] = array[r]
    array[r] = swap
    return i+1

data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
 
size = len(data)
 
quicksort(data, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(data)