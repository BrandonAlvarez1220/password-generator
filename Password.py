import string
import random

class Password:

    def __init__(self, length):
        self.length = length

    # Boolean values to enable or disable the generation of:
    # sc -> Special characters
    # l -> Letters
    # n -> Numbers
    def generate(self, sc=True, let=True, n=True):

        # Add any letter
        letters = string.ascii_letters

        # Add special characters
        specialChar = string.printable[64:93]

        password = ''

        for i in range(self.length):

            if not let and not n and not sc:
                return ''

            if not let and not n:
                number = 2
            elif not let and not sc:
                number = 1
            elif not n and not sc:
                number = 0
            else:
                if not let:
                    number = random.choice([1, 2])
                elif not n:
                    number = random.choice([0, 2])
                elif not sc:
                    number = random.choice([0, 1])
                else:
                    number = random.randint(0, 2)

            match number:

                # Case 0 add a letter
                case 0:
                    password += random.choice(letters)

                # Case 1 add a number
                case 1:
                    password += str(random.randint(0, 9))

                # Case 2 add a special character
                case 2:
                    password += random.choice(specialChar)

                # No element
                case _:
                    password += ''

        return password

    def cipherPassword(self, password, key):

        password_list = list(password)
        password_lenght = len(password_list)

        for i in range(password_lenght):
            index = (i-key) % password_lenght
            password_list[i] = password[index]

        return ''.join(password_list)


    def decipherPassword(self, password, key):

        password_list = list(password)
        password_lenght = len(password_list)

        for i in range(password_lenght):
            index = (i+key) % password_lenght
            password_list[i] = password[index]

        return ''.join(password_list)
