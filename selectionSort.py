# Two functions are defined to create the selection sort algorithm

# initial function takes care of finding the smallest value in an array, written the following way:

# define the function, array as an argument
def find_smallest(arr):
    smallest = arr[0]  # define 'smallest' var, assuming that the initial array element is the smallest
    smallest_index = 0  # define 'smallest_index' var, assuming that initial index is for the smallest
    for i in range(1, len(arr)):  # For loop beginning in index 1 of the array to the length of such
        if arr[i] < smallest:  # if the current array position is less than smallest
            smallest = arr[i]  # update the array position
            smallest_index = i  # update the index position of smallest value
    return smallest_index  # returning a single value, the position of the index of the smallest val


# Define the selection sort function, that will use the previous function created

def selection_sort(arr):  # function define, passing an array as an argument
    new_array = []  # defining a new empty array
    for i in range(len(arr)):  # looping over the length of the array
        smallest = find_smallest(arr)  # var of smallest value = the function previously created in action
        new_array.append(arr.pop(smallest))  # adding result after finding it, and removing it from the old array.
    return new_array    # return the newly created and sorted array

# defining old_array and printing results


old_array = [5, 3, 6, 2, 10]

#print('old array: ')
#print(old_array)
##print('new sorted array: ')
#print(selection_sort([5, 3, 6, 2, 10]))

#print(selection_sort([2,1] + [3] + selection_sort([5,4])))

sort_this = selection_sort([1,3,7,9]) + [5]
print(sort_this)
final_Sort = selection_sort(sort_this)
print(final_Sort)