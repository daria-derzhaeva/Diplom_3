from faker import Faker

fake = Faker()

def generate_user_data():
    return {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
    }
