class Solution:
    def Power(self, base, exponent):
        mul=1
        if (exponent>=0):
            for i in range(exponent):
                mul*=base
        else:
            for i in range(-1*exponent):
                mul*=base
            mul=1/mul
        return mul
