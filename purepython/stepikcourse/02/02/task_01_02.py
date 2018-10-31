from simplecrypt import decrypt, DecryptionException

from os.path import exists
from os import unlink

# this is an example program that reads and writes encrypted files.

# if the file "encrypted.txt" does not exist, then it is created with
# the contents "10 green bottles".

# if the file does exist, is is read, and the number of green bottles
# is reduced.  if there are no green bottles left, then the file is
# deleted, otherwise it is written with the new number.

import sys

PASSWORDSFILENAME = "passwords.txt"
MESSAGEFILENAME = "encrypted.bin"
sys.stdin = open(PASSWORDSFILENAME, "r")

def main():


    while True:
        try:
            passwd = str(input())
        except EOFError:
            break
        else:
            if exists(MESSAGEFILENAME):
                print("reading...")

                try:
                    data = read_encrypted(passwd, MESSAGEFILENAME)
                except DecryptionException:
                    print("Password %s is not right" % (passwd))
                else:
                    print("Decrypted message is: %s" % (data))
                    break
#                finally:
#                    unlink(MESSAGEFILENAME)


def read_encrypted(password, filename, string=True):
    with open(filename, 'rb') as input:
        ciphertext = input.read()
        plaintext = decrypt(password, ciphertext)
        if string:
            return plaintext.decode('utf8')
        else:
            return plaintext

if __name__ == '__main__':
    main()