import string
import random

def generate_random_string(length=6):
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


bank_library = [("Лев Толстой","Война и мир") , ("Сергей Довлатов","Чемодан") ,
                ("Маша Трауб", "Дневник мамы первоклассника"), ("Теодор Драйзер", "Американская трагедия"),
                ("Теодор Дразйер", "Финансист"), ("Сергей Довлатов","Заповедник")]

def return_random_book():
    return random.choice(bank_library)

