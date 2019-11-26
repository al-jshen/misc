from rsa import init, encrypt, decrypt

p = 61
q = 53
n, e = init(p, q)
encrypted = [encrypt(n, e, ord(i)) for i in input()]
print(encrypted)
decrypted = [chr(decrypt(n, e, p, q, j)) for j in encrypted]
print("".join(decrypted))

