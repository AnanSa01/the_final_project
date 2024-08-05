import random
import string


class Utilities:

    @staticmethod
    def generate_random_string_with_numbers_and_punctuation(length):
        letters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def generate_random_string_text_with_numbers(length):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def generate_random_string_just_text(length):
        letters = string.ascii_letters
        return (''.join(random.choice(letters) for _ in range(length))).capitalize()

    @staticmethod
    def generate_random_string_just_numbers(length):
        letters = string.digits
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def generate_random_string_just_punctuation(length):
        letters = string.punctuation
        return ''.join(random.choice(letters) for _ in range(length))

