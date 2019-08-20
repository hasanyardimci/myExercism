import random
import datetime


class Robot(object):

    def __init__(self):
        self.alpha1 = self.alpha2 = ['A', 'B', 'C', 'D', 'E', 'E', 'E', 'F', 'G', 'H', 'H',
                                     'I', 'J', 'K', 'L', 'M', 'N', 'O', 'O', 'O', 'O', 'P',
                                     'Q', 'R', 'R', 'S', 'T', 'T', 'U', 'U', 'V', 'W', 'X', 'Y', 'Z']

        self.num1 = self.num2 = self.num3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def name(self):
        dt = datetime.datetime.now()
        random.seed(dt.year + dt.month + dt.day + dt.hour + dt.minute + dt.second + dt.microsecond)
        ismi = (random.choice(self.alpha1) +
                random.choice(self.alpha2) +
                random.choice(self.num1) +
                random.choice(self.num2) +
                random.choice(self.num3))
        return ismi

    def reset(self):
        self.name()
