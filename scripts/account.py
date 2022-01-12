from unicodedata import name


class Account:
    """"""
    def __init__(self, id, name, institution, date_opened, type, balance, limit) -> None:
        self.id = id
        self.name = name
        self.institution = institution
        self.date_opened = date_opened
        self.type = type
        self.balance = balance
        self.limit = limit

    def create(self):
        pass

    def modify(self):
        pass

    def update_balance(self, amount):
        pass
        