def max_num(lis):
    if len(lis) == 1:
        return lis[0]
    else:
        return max(lis[0], max_num(lis[1:]))

lista = [1, 3, 9]
print("Maximum number in the list:", max_num(lista))