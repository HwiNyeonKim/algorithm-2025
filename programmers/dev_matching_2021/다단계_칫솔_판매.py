class Employee:
    def __init__(self, name, referral):
        self.name = name
        self.referral = referral
        self.net_profit = 0

    def settle(self, profit):
        tribute = profit // 10
        self.net_profit += profit - tribute
        return tribute


def solution(enrolls, referrals, sellers, amount_list):
    employees = dict()
    employees["-"] = Employee("-", None)

    for name, referral_name in zip(enrolls, referrals):
        referral = employees[referral_name]
        employees[name] = Employee(name, referral)

    for seller, amount in zip(sellers, amount_list):
        profit = 100 * amount

        employee = employees[seller]
        tribute = employee.settle(profit)

        referral = employee.referral
        while referral and tribute:
            tribute = referral.settle(tribute)
            referral = referral.referral

    return [employees[name].net_profit for name in enrolls]
