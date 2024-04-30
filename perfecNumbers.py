def sumOfFactor(number):
    sum = 0
    for i in range(1, number + 1):
        if (number % i == 0):
            sum += i
    return sum


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer

    if sum of factors equal number
    return "Perfect"
    if sum of factors > number
    return 'Abundant'
    if sun of factor < number
    return 'Incomplete'
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    if number == sumOfFactor(number):
        return "perfect"
    if sumOfFactor(number) <= number:
        return "deficient"
    if sumOfFactor(number) >= number:
        return "abundant"
    return

print(classify(6))
print(sumOfFactor(12))