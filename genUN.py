import random
import string

user_FN = input('Enter your First name : ')
fav_num = input('Enter your favorite number : ')
password = ''.join(random.choice(user_FN + fav_num) for i in range(8))
print(password)
