def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    percentage_value = (generated_power / theoretical_max_power) * 100

    if percentage_value > 80:
        print('green')
    elif percentage_value < 80 and percentage_value > 60:
        print('orange')
    elif percentage_value < 60 and percentage_value > 30:
        print('red')
    elif percentage_value < 30:
        print('black')


reactor_efficiency(10, 1000, 10000)


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    neu_temp = temperature * neutrons_produced_per_second
    minus_10p = threshold * 1.1
    plus_10p = threshold * 0.9

    if neu_temp < threshold * .4:
        return "LOW"
    if minus_10p <= neu_temp <= plus_10p:
        return "NORMAL"
    return "DANGER"


print(fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000))


def value_of_card(card):
    if card == 'J' or card == 'Q' or card == 'K':
        return 10
    if card == 'A':
        return 1
    return int(card)


def value_of_ace(card_one, card_two):
    if value_of_card(card_one) + value_of_card(card_two) > 11:
        return 1
    elif value_of_card(card_one) + value_of_card(card_two) < 11:
        return 11


print(value_of_card('A') + value_of_card('2'))
print(value_of_ace('A', '2'))


def can_double_down(card_one, card_two):
    lucky_numbers = {9, 10, 11}
    if value_of_card(card_one) + value_of_card(card_two) in lucky_numbers:
        return True
    return False


print(can_double_down('2', '2'))


def make_word_groups(vocab_words):
    world_groups = (' :: ' + vocab_words[0]).join(vocab_words)
    return world_groups


print(make_word_groups(['en', 'close', 'joy', 'lighten']))


def remove_suffix_ness(word):
    return word[:-4] if word[-5] != 'i' else word[:-5] + 'y'


print(remove_suffix_ness("heaviness"))
###############
input_data = ['Look at the bright sky.',
              'His expression went dark.',
              'The bread got hard after sitting out.',
              'The butter got soft in the sun.',
              'Her eyes were light blue.',
              'The morning fog made everything damp with mist.',
              'He cut the fence pickets short by mistake.',
              'Charles made weak crying noises.',
              'The black oil got on the white dog.']
index_data = [-2, -1, 3, 3, -2, -3, 5, 2, 1]


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    # grab the index and = 'en'
    return sentence.split()[index].strip('.') + 'en'


sentence = "It got dark as the sun set."
print(adjective_to_verb(sentence, 2))

nums = [-4, -1, 0, 3, 10]


def sortedSquares(nums):
    res = []
    l, r = 0, len(nums) -1
    while l <= r:
       if nums[l] * nums[l] > nums[r] * nums[r]:
        res.append(nums[l] * nums[l])
        l = l + 1
       else:
        res.append(nums[r] * nums[r])
        r = r - 1
    return res[:: -1]


print(sortedSquares(nums))



def sumFactors(number):
    res = 0
    for i in range(1, number + 1):
        if (number % i == 0):
            res += i
    return res


def sumOfFactor(number):
    asd = 0
    for i in range(1, number + 1):
        if (number % i == 0):
            asd += i
    return asd

print(sumOfFactor(12))

print(sumFactors(1))