# You define the function name
# you define the low and high variables, the star and end of the lists
# inside the function you define a while loop
# while start point is less than the value at the end point
# define middle variable which is a sum of the start and end point
# define the guess variable which is the value mid as an index in the list
# create an if statement, if guessed answer is equal to the item (which is the actual answer)
# return the value of mid which is the index where such value is found
# create another if statement, if the guessed answer is greater than the actual result, then the end point lowers by 1
# create an else statement in case the guess value is less than the item value
# update low variable to 'mid' value plus one
# if nothing is found print return None

# To test such, you create a list with some numbers, in organized manner, MUST BE ORGANIZED After creating the list,
# you print the method, while passing the arguments (the list and the number that you are looking for)


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low+high)
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
            print("Nothing found")
            return None


my_list = [3, 6, 9, 12, 15, 16]

print(binary_search(my_list, 12))