class Employee:
    def __init__(self, name, referral):
        self.name = name
        self.referral = referral
        self.amount = 0
        self.subordinates = list()
        self.net_profit = 0

    def settle(self):
        profit = 100 * self.amount

        for subordinate in self.subordinates:
            profit += subordinate.settle()

        tribute = profit // 10
        self.net_profit = profit - tribute

        return tribute

    def get_net_profit(self):
        return self.net_profit


def solution(enrolls, referrals, sellers, amount_list):
    employees = dict()

    minho = Employee("-", None)
    employees["-"] = minho

    for name, referral_name in zip(enrolls, referrals):
        referral = employees[referral_name]
        subordinate = Employee(name, referral)

        employees[name] = subordinate
        referral.subordinates.append(subordinate)

    for seller, amount in zip(sellers, amount_list):
        employees[seller].amount += amount

    minho.settle()

    return [employees[name].get_net_profit() for name in enrolls]
