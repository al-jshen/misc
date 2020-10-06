# Euclidean algorithm for computing greatest common divisor.


def gcd(a, b):

    if b >= a:
        a, b = b, a

    r0 = a % b
    if r0 == 0:
        return b

    r1 = b % r0
    if r1 == 0:
        return r0

    if r0 > 0 and r1 > 0:
        rk_2 = r0
        rk_1 = r1
        rk = rk_2 % rk_1
        while rk > 0:
            print(rk, rk_1, rk_2)
            rk_2 = rk_1
            rk_1 = rk
            rk = rk_2 % rk_1
        else:
            return rk_1


print(gcd(int(input()), int(input())))
