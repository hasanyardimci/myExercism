def is_armstrong_number(number):
    dg = len(str(number))
    for i in str(number):
        number -= int(i) ** dg
    if number == 0:
        return True
    else:
        return False