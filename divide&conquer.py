def sum(arr):
    if arr == []:
        return 0  # BASE CASE
    return arr[0] + sum(arr[1:])  # RECURSIVE CASE


le_test = [2, 4, 6]

print(sum(le_test))