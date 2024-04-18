book = {}
my_array = [1,2,3,4]
lenght = len(my_array)


def print_array(arr):
    for i in range(lenght-3):
        print(my_array[i])
        print(arr.index(arr[i]))


print(print_array(my_array))