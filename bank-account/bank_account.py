import sys
import threading
import time

class BankAccount(object):

    def __init__(self):
        self.balance = 0
        self.acc_status = 2 # 0 is open, 1 is closed, 2 inactive/init

    def get_balance(self):
        if self.acc_status == 0:
            return self.balance
        else:
            raise ValueError('Account closed')

    def open(self):
        if self.acc_status == 0:
            raise ValueError("Already opened account")
        else:
            self.acc_status = 0
            self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Value Error; Negatif Amount')
        else:
            if self.acc_status == 0:
                self.balance += amount
            else:
                raise ValueError('Account closed')

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError('Value Error; Negatif Amount')
        else:
            if self.acc_status == 0:
                self.balance -= amount
                if self.balance < 0:
                    raise ValueError
            else:
                raise ValueError('Account closed')

    def close(self):
        if self.acc_status != 1:
            self.acc_status = 1
        else:
            raise ValueError('Account already closed')