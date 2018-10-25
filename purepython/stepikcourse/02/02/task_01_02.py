from simplecrypt import encrypt, decrypt

plaintext = decrypt('password', ciphertext)

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("passwords.t xt", "r") as psw:
    passwords = psw.read()

mystring = decrypt('password', ciphertext).decode('utf8')

print(passwords)