from __future__ import division

class Rational(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def f_multiple(self, nmbr):
        multiple_list = []
        for b in range(2, nmbr + 1):
            while nmbr % b == 0 and nmbr >= b:
                nmbr /= b
                multiple_list.append(b)
        return multiple_list

    def find_gcd(self, n1, n2):
        m1 = self.f_multiple(abs(n1))
        m2 = self.f_multiple(abs(n2))
        gcd_list = []
        if abs(n1) <= abs(n2):
            while len(m1) > 0:
                if m1[0] in m2:
                    gcd_list.append(m1[0])
                    m2.remove(m1[0])
                m1.pop(0)
        else:
            while len(m2) > 0:
                if m2[0] in m1:
                    gcd_list.append(m2[0])
                    m1.remove(m2[0])
                m2.pop(0)
        gcd = 1
        for i in gcd_list:
            gcd *= i
        return gcd

    def __eq__(self, other):
        if self.numer == 0:
            self.denom = 1
        else:
            gcd = self.find_gcd(self.numer, self.denom)
            self.numer //= gcd
            self.denom //= gcd
            if self.denom < 0:
                self.numer *= -1
                self.denom *= -1
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        if self.numer == 0:
            self.denom = 1
        else:
            gcd = self.find_gcd(self.numer, self.denom)
            self.numer //= gcd
            self.denom //= gcd
            if self.denom < 0:
                self.numer *= -1
                self.denom *= -1
        return '{}/{}'.format(self.numer, self.denom)

    def to_fl(self):
        if self.numer == 0:
            self.denom = 1
        else:
            gcd = self.find_gcd(self.numer, self.denom)
            self.numer //= gcd
            self.denom //= gcd
            if self.denom < 0:
                self.numer *= -1
                self.denom *= -1
        return self.numer/self.denom

    def __add__(self, other):
        if self.denom != other.denom:
            a = self.numer * other.denom + other.numer * self.denom
            if a != 0:
                b = self.denom * other.denom
                gcd = self.find_gcd(a, b)
                a /= gcd
                b /= gcd
            else:
                a = 0
                b = 1
        else:
            a = self.numer + other.numer
            if a != 0:
                b = self.denom
                gcd = self.find_gcd(a, b)
                a /= gcd
                b /= gcd
            else:
                a = 0
                b = 1
        return Rational(int(a), int(b))

    def __sub__(self, other):
        if self.denom != other.denom:
            a = self.numer * other.denom - other.numer * self.denom
            if a != 0:
                b = self.denom * other.denom
                gcd = self.find_gcd(a, b)
                a /= gcd
                b /= gcd
            else:
                a = 0
                b = 1
        else:
            a = self.numer - other.numer
            if a != 0:
                b = self.denom
                gcd = self.find_gcd(a, b)
                a /= gcd
                b /= gcd
            else:
                a = 0
                b = 1
        return Rational(int(a), int(b))

    def __mul__(self, other):
        a = self.numer * other.numer
        if a != 0:
            b = self.denom * other.denom
            gcd = self.find_gcd(a, b)
            a /= gcd
            b /= gcd
            if b < 0:
                a *= -1
                b *= -1
        else:
            a = 0
            b = 1
        return Rational(int(a), int(b))

    def __truediv__(self, other):
        a = self.numer * other.denom
        if a != 0:
            b = self.denom * other.numer
            gcd = self.find_gcd(a, b)
            a /= gcd
            b /= gcd
            if b < 0:
                a *= -1
                b *= -1
        else:
            a = 0
            b = 1
        return Rational(int(a), int(b))

    def __abs__(self):
        if self.numer < 0:
            self.numer = self.numer * -1
        if self.denom < 0:
            self.denom = self.denom * -1
        return Rational(self.numer, self.denom)

    def __pow__(self, power):
        if power >= 0:
            a = self.numer ** power
            b = self.denom ** power
        else:
            a = self.denom ** power
            b = self.numer ** power
        return Rational(int(a), int(b))

    def __rpow__(self, base):
        a = Rational(self.numer,self.denom).to_fl()
        return base ** a