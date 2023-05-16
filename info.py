from faker import Faker
import colorama
from random import *
faker = Faker("fa_IR")
username = faker.user_name()
password = faker.password()
email = faker.email()
job = faker.job()
address = faker.address()
favorite_color = faker.color_name()
def national_code_generator():
    number_list = []
    ethr = 1
    m1 = ""
    for i in reversed(range(2, 11)):
        he = randint(0, 9)
        number_list.append(str(he))
        ethr += he * i
    lo = ethr % 11
    if lo < 2:
        number_list.append(str(lo))
    elif lo >= 2:
        number_list.append(str(11 - lo))
    return m1.join(number_list)
national_code = national_code_generator()
print("Username : {}\n".format(username))
print("Password : {}\n".format(password))
print("Email : {}\n".format(email))
print("Work : {}\n".format(job))
print("Address : {}\n".format(address.replace("\n","")))
print("Favorite Color : {}\n".format(favorite_color))
print("National Code : {}\n".format(national_code))
