

def quicksort(arr):
    if len(arr) < 2:
        return arr  # BASE CASE returns arr if...
    else:
        pivot = arr[0]  # pivot variable will be initial index
        less = [i for i in arr[1:] if i <= pivot]  # list of lesser items than pivot
        greater = [i for i in arr[1:] if i > pivot]  # list of greater items than pivot

    return quicksort(less) + [pivot] + quicksort(greater)  # both less and great sorted with the pivot in the middle


array = [10, 5, 2, 3]

print(quicksort(array))
