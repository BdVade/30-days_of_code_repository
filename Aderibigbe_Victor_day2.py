import random


def password_generator(password_length):
    """This a function to generate a random alphanumeric password of a specified length"""
    if password_length < 8:
        return "Your password is weak"
    character_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                      'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
                      'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                      'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    password = ""
    for i in range(password_length):
        placeholder = random.choice(character_list)
        password = password + placeholder

    return password


x = password_generator(8)
print(x)
