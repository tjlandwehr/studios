# FRACTION¶

# A fraction has a numerator and denominator. A fraction should be able to add itself to another fraction, 
# returning a new fraction that represents the sum. A fraction should be able to multiply itself by another 
# fraction, returning a new fraction as the product. A fraction should be able to take the reciprocal of 
# itself, returning that value as a new fraction. A fraction should be able to simplify itself, returning a new 
# fraction as that simplification.

def find_gcd(numerator, denominator):
    while numerator % denominator != 0:
        old_num = numerator
        old_den = denominator

        numerator = old_den
        denominator = old_num % old_den

    return denominator

class Fraction:

    def __init__(self, top, bottom):

        self.num = top      # the numerator is on top
        self.den = bottom   # the denominator is on the bottom

    def __repr__(self):
        return str(self.num) + "/" + str(self.den)

    def get_numerator(self):
        return self.num

    def get_denominator(self):
        return self.den

    def add(self,rhs):

        new_num = self.num * rhs.den + self.den * rhs.num
        new_den = self.den * rhs.den

        return Fraction(new_num, new_den).simplify()

    def mult(self, rhs):
        new_num = self.num * rhs.num
        new_den = self.den * rhs.den

        return Fraction(new_num, new_den).simplify()

    def recip(self):
        return Fraction(self.den, self.num).simplify()

    def simplify(self):
        common = find_gcd(self.num, self.den)

        return Fraction(self.num // common, self.den // common)

def main():
    myfraction = Fraction(12, 18)
    other_fraction = Fraction(1, 2)
    print('my frac: ', myfraction)
    print('other frac: ', other_fraction)

    print('get num: ', myfraction.get_numerator())
    print('get denom: ', myfraction.get_denominator())
    print('add: ', myfraction.add(other_fraction))
    print('multiply: ', myfraction.mult(other_fraction))
    print('get reciprocal: ', myfraction.recip())
    print('get simple: ', myfraction.simplify())

if __name__ == "__main__":
    main()