from faker import Faker

fake = Faker()
# print(dir(fake))

di={}

for i in range(20):
    di[fake.name()] = fake.name()
    di[fake.email()] = fake.email()
    di[fake.address()] = fake.address()
    di[fake.phone_number()] = fake.phone_number()
    di[fake.password()] = fake.password()
    di[fake.date()] = fake.date()

print(di,end=",")
