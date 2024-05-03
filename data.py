import faker
from config import NAMES
import random
def registration_data():
    fake = faker.Faker()
    email = fake.email()
    password = fake.password()
    random_number = random.randint(0, len(NAMES)-1)
    name = NAMES[random_number]
    return name, email, password