import random
import string


def password(length=28):
    your_letters='ABCDEFGHIJKLMOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+=[{]}\|;:,<.>/?'
    return ''.join((random.choice(your_letters) for i in range(length)))
def main():
    running = 1
    while running == 1:
        print(password())
        wait = input ("")
main()
