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


print(exchangeable_value(127.25, 1.20, 10, 20))
