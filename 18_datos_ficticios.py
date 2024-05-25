from faker import Faker

fake = Faker()

print(fake.name())
print(fake.address())
print(fake.text())
print(fake.email())
print(fake.phone_number())
print(fake.date_of_birth())
print('*'*25)
perfil = fake.profile()
print(perfil)
print('*'*25)
# con localizacion especifica
fake_es = Faker('es_ES')
print(fake_es.name())
print(fake_es.address())
