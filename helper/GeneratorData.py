from faker import Faker

fake = Faker()
class GeneratorData:

    def __init__(self):
        self.name = fake.first_name()
        self.due_date = fake.random_int(max=99999)
        self.description = fake.word()
        self.multiple_owners = fake.boolean()
        self.color = fake.color_name()