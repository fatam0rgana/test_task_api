def validate_amount(amount):
    try:
        amount = float(amount)
        return isinstance(amount, float) and amount >= 1 and (amount % 1 >= 0.01 or amount % 1 == 0)
    except:
        return False


def validate_currency(currency):
    return currency in ('643', '840', '978')
