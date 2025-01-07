class Employee:
    def __init__(self, name, referral):
        self.name = name
        self.referral = referral
        self.net_profit = 0

    def settle(self, profit):
        tribute = profit // 10

        self.net_profit += profit - tribute
        if self.referral:
            self.referral.settle(tribute)

    def get_net_profit(self):
        return self.net_profit


def solution(enrolls, referrals, sellers, amount_list):
    employees = dict()

    minho = Employee("-", None)
    employees["-"] = minho

    for name, referral_name in zip(enrolls, referrals):
        referral = employees[referral_name]
        employees[name] = Employee(name, referral)

    for seller, amount in zip(sellers, amount_list):
        profit = 100 * amount
        employees[seller].settle(profit)

    return [employees[name].get_net_profit() for name in enrolls]
