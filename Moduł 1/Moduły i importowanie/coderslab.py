from random import randint

words = ["hello", "darkness", "my", "old", "friend"]


def coderslab_welcome():
    return "Welcome to CodersLab!"

def random_word():
    the_random_thing = randint(0, 4)
    return words[the_random_thing]
