from faker import Faker
from random import randrange, choice
from .models import Cliente



def create_pessoas(q):
    faker = Faker('pt-BR')
    for _ in range(q):
        nome = str(faker.name())
        cpf = (faker.cpf())
        celular = randrange(95632145610)
        emai = f'{nome.replace(" ", "").lower()}@{faker.free_email_domain()}' 
        ativo = choice([True, False])
        rg = randrange(326547896)
        cliente = Cliente(nome=nome, cpf=cpf, celular=celular, email=emai, ativo=ativo, rg=rg)
        cliente.save()

