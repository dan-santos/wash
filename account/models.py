from django.db import models
from user.models import CustomUser

class Address(models.Model):
    city = models.CharField('Cidade', max_length=50)
    district = models.CharField('Bairro', max_length=100)
    street = models.CharField('Rua', max_length=255)
    number = models.CharField('Número', max_length=50)
    cep = models.CharField('CEP', max_length=8)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __repr__(self) -> str:
        return f'{self.street}, {self.number}. {self.district} - {self.city}, {self.cep}'


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='Usuário')
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, verbose_name='Endereço')
    vehicle_type = models.CharField('Tipo de veículo', max_length=8, choices=(
        ('Carro', 'Carro'),
        ('Moto', 'Moto'),
        ('Caminhão', 'Caminhão'),
        ('Van', 'Van'),
        ('Ônibus', 'Ônibus'),
    ))
    carrier = models.BooleanField('Com caçamba', default=False)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    def __repr__(self) -> str:
        return self.user.get_full_name