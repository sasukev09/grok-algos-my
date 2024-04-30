def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    actual_rate = exchange_rate + (exchange_rate * (spread / 100))
    exchanged_value = (int(denomination * (budget / actual_rate))) / denomination

    print(exchanged_value)
    bills_exchanged = exchanged_value // denomination
    print(bills_exchanged)

    end_value = bills_exchanged * denomination
    return end_value


# print(exchangeable_value(127.25, 1.20, 10, 20))


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    average = sum(hand) / len(hand)
    return average


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    average1 = (hand[0] + hand[-1]) / 2
    median = hand[len(hand) // 2]

    if average1 == card_average(hand) or median == card_average(hand):
        return True
    return False


hand = [0, 2, 3]
print(approx_average_is_average([0, 2, 3]))

print(hand[-1])

hand1 = [1, 2, 11]


def maybe_double_last(hand1):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand1[-1] == 11:
        hand1[-1] = hand1[-1] * 2
        return hand1
    else:
        return print("uhhhhhhhh")


# print(maybe_double_last(hand1))

def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue: list - names in the normal queue.
    :param ticket_type: int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """
    if express_queue and ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    elif normal_queue and ticket_type == 0:
        normal_queue.append(person_name)
    return normal_queue


print((add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=1,
                           person_name="RichieRich")))

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    return threshold <= [score for score in student_scores]