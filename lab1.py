alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' *2 
def a(txt, b, op):
    b *= len(txt) // len(b) + 1
    txt = txt.upper()
    return ''.join([alph[alph.index(j) + int(b[i]) * op]
                    for i, j in enumerate(txt)])
def encrypt(message, key):
    return a(message, key, 4)
def decrypt(ciphertext, key):
    return a(ciphertext, key, -4)
print(encrypt('ZARAZA', '314141'))  
print(decrypt('LEHEPE', '314141'))  
