class Flatmate:
    """
    Creates a person who lives in the flat and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house


class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

    # Calculates how much every flatmate has to pay.

    def to_pay(self, lst: list[Flatmate]) -> dict:
        split_bill = dict()

        # Value of a day for every flatmate

        weight = self.amount / sum([i.days_in_house for i in lst])

        # Adds the name and the sum to pay for every flatmate

        for i in lst:
            split_bill[i.name] = round(i.days_in_house * weight, 2)
        return split_bill
