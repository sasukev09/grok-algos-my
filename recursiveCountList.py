# Write a recursive function
# To count the No of items in a list

def countList(lis):
    if lis == []:
        return 0
    return 1 + countList(lis[1:])

le_test = [1,3,9,2]
print(countList(le_test))

