def is_isogram(string):
    low_string = string.lower()
    list = []

    for char in low_string:

        if char.isalpha():

            if char in list:
                return False

            else:
                list.append(char)

    return True



def is_isogram(word):
    word = word.lower().replace(" ","").replace("-","")
    return len(word) == len(set(word))