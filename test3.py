dict = {"Black": 0, "Brown": 1, "Red": 2, "Orange": 3, "Yellow": 4, "Green": 5, "Blue": 6, "Violet": 7, "Grey": 8, "White": 9}


def color_code(color):
    return dict.get(color)


def colors():
    return dict.keys()


#print(color_code("Brown"))
#print(colors())

def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    count = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        count += 1
    return count


print(steps(12))



s = []
s.append(1)
print(s)
s.append(2)
print(s)



def sortedSquares(nums):
    res = []

    l, r = 0, len(nums) - 1


    while l <= r:
        l_sq = nums[l] * nums[l]
        r_sq = nums[r] * nums[r]
        if l_sq > r_sq:
            res.append(l_sq)
            l += 1
        else:
            res.append(r_sq)
            r -= 1
    return res[::-1]

print(sortedSquares([-4,-1,0,3,10]))