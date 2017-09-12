import SDES
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage:")
        print("Encrypting: python3 {} -e".format(sys.argv[0]))
        print("Decrypting: python3 {} -d".format(sys.argv[0]))
        sys.exit()

    if sys.argv[1] == "-e":
        P = input("Plaintext (8 bit): ")
        K = input("Key (10 bit): ")
        print("Ciphertext: {}".format(SDES.encrypt(P, K)))
    elif sys.argv[1] == "-d":
        C = input("Ciphertext (8 bit): ")
        K = input("Key (10 bit): ")
        print("Plaintext: {}".format(SDES.decrypt(C, K)))
