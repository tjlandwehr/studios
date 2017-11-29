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

    def __init__(self, init_numerator, init_denominator):
        self.numerator = init_numerator
        self.denominator = init_denominator
    
    def __repr__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator
    
    def factors(self, factor):
        divisor_list = []
        for n in range(1, factor + 1):
            if factor % n == 0:
                divisor_list.append(n)
        return divisor_list

    def is_prime(self, num):
        return len(self.factors(num)) == 2

    def prime_factors(self, num):
        self_factors = self.factors(num)
        prime_list = []
        for self_factor in self_factors:
            if self.is_prime(self_factor):
                prime_list.append(self_factor)
        return prime_list

    def common_prime_factors(self, self_list, target_list):
        common_prime_list = []
        if len(self_list) > 0:
            for prime_num in self_list:
                if prime_num in target_list:
                    common_prime_list.append(prime_num)
            return common_prime_list
        else:
            common_prime_list.append(1)
            return common_prime_list
    
    def least_common_multiple(self, num_1, num_2):
        num_1_multiples = []
        num_2_multiples = []
        common = False
        counter = 0
        while not common:
            num_1_multiples.append(num_1 * (counter + 1))
            num_2_multiples.append(num_2 * (counter + 1))
            if num_1_multiples[counter] in num_2_multiples:
                return num_1_multiples[counter]
            if num_2_multiples[counter] in num_1_multiples:
                return num_2_multiples[counter]
            counter += 1
    
    def simplify_fraction(self):
        common = find_gcd(self.numerator, self.denominator)

        self.numerator = self.numerator // common
        self.denominator = self.denominator // common
        # num_factors = self.factors(self.numerator)
        # denom_factors = self.factors(self.denominator)
        # greatest_common_factor_list = []
        # for factor in num_factors:
        #     if factor in denom_factors:
        #         greatest_common_factor_list.append(factor)
        # greatest_common_factor = greatest_common_factor_list[len(greatest_common_factor_list) - 1]
        # self.numerator = int(self.numerator / greatest_common_factor)
        # self.denominator = int(self.denominator / greatest_common_factor)
    
    def __add__(self, fraction2):

        new_num = self.numerator * fraction2.denominator + self.denominator * fraction2.numerator
        new_den = self.denominator * fraction2.denominator

        common = find_gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

    def add_fraction(self, target):
        new_num = self.numerator * target.denominator + self.denominator * target.numerator
        new_den = self.denominator * target.denominator

        common = find_gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)
        # if self.denominator == target.denominator:
        #     return Fraction(self.numerator + target.numerator, self.denominator)
        # else:
        #     lcm = self.least_common_multiple(self.denominator, target.denominator)
        #     self_multiple = int(lcm / self.denominator)
        #     target_multiple = int(lcm / target.denominator)
        #     new_numerator = self.numerator * self_multiple + target.numerator * target_multiple
        #     # num_prime_list = self.prime_factors(new_numerator)
        #     # denom_prime_list = self.prime_factors(lcm)
        #     # common_prime_factors = self.common_prime_factors(num_prime_list, denom_prime_list)
        #     # greatest_common_factor = 1
        #     # for i in range(len(common_prime_factors)):
        #     #     greatest_common_factor *= common_prime_factors[i]
        #     # final_numerator = int(new_numerator / greatest_common_factor)
        #     # final_denominator = int(lcm / greatest_common_factor)
        #     added_fraction = Fraction(new_numerator, lcm)
        #     added_fraction.simplify_fraction()
        #     return added_fraction

def main():
    p = Fraction(3, 18)
    q = Fraction(5, 24)
    print("Fraction p =", p)
    print("Fraction q =", q)
    g = q.add_fraction(p)
    print("Fractions p + q =", g)
    print(p + g)
    # print(g.numerator, g.denominator)

if __name__ == "__main__":
    main()