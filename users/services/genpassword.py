import string, random

def generatePassword():
    num = 8
    password = ''

    for _ in range(num):
        x = random.randint(0, 35)
        password += string.printable[x]

    return password