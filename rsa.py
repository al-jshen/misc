from euclidean import gcd

def init(p, q):
    """ Initiate algorithm given two (large) distinct primes p, q
    n and e are announced to the public
    phi_n is kept private
    """
    n = p * q
    phi_n = (p-1) * (q-1)
    for i in range(2, 100):
        if gcd(i, phi_n) == 1:
            e = i
            break
    return n, e

def encrypt(n, e, m):
    """ Given a message m < n, return an encrypted form of the message
    """
    return m ** e % n

def decrypt(n, e, p, q, r):
    """ Decrypt a message
    Need to find a d>=0 such that de + k*phi(n) = 1 
    """
    phi_n = (p-1) * (q-1)
    for i in range(10000):
        if i*e % phi_n == 1:
            d = i
            break
    return r ** d % n

p = 61
q = 53
n, e = init(p, q)
print(n, e)
m = 1245
print(m)
enc = encrypt(n, e, m)
print(enc)
dec = decrypt(n, e, p, q, enc)
print(dec)

