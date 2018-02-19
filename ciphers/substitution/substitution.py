import random

def substitution(plaintext):
    letters = range(26)
    random.shuffle(letters)
    cipher = plaintext
    for i in range(26):
        pt = chr(65+i)
        cipher = cipher.replace(pt, chr(97+letters[i]))
    return cipher, letters

print substitution("abcthisisatestmessage".upper())
