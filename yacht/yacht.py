"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"


def is_full_house(dice):
    k = []
    for i in (1,2,3,4,5,6):
        k.append(dice.count(i))
    print (k)
    if k.count(3) == 1 and k.count(2) == 1:
        return True
    else:
        return False

def is_four_of_a_kind(dice):
    i = 1
    while i < 7:
        if dice.count(i) >= 4:
            return 4*i
        else:
            i += 1
    return 0

def score(dice, category):
    a = []
    for i in (1,2,3,4,5,6):
        a.append(dice.count(i)*i)
    if category == "ONES":
        return a[0]
    elif category == "TWOS":
        return a[1]
    elif category == "THREES":
        return a[2]
    elif category == "FOURS":
        return a[3]
    elif category == "FIVES":
        return a[4]
    elif category == "SIXES":
        return a[5]
    elif category == "FULL_HOUSE" and is_full_house(dice):
        return sum(dice)
    elif category == "FOUR_OF_A_KIND":
        return is_four_of_a_kind(dice)
    elif category == "LITTLE_STRAIGHT" and sum(dice) == 15:
        return 30
    elif category == "BIG_STRAIGHT" and sum(dice) == 20:
        return 30
    elif category == "CHOICE":
        return sum(a)
    elif category == "YACHT" and sum(dice) == dice[0]*5:
        return 50
    else:
        return 0
