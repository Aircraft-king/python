class Account:
    def __init__(self,id,balance,rate):
        self.id = id
        self.balance = balance
        self.rate = rate
    def DepositMoney(self,money):
        self.balance -= money
    def TakeMoney(self,money):
        self.balance += money
    def MonthRate(self):
        return self.rate/12.00
    def MonthInterest(self):
        return self.balance * self.MonthRate() * 0.01
acc = Account(998866,2000,4.5)
acc.TakeMoney(150)
acc.DepositMoney(1500)
print('账号: %d' % acc.id)
print('余额: %.2f' % acc.balance)
print('年利率: %.2f%%' % acc.rate)
print('月利率：%.2f%%' % acc.MonthRate())
print('月息：%.2f' % acc.MonthInterest())