from django.db.models import *

class Model_request(Model):

    name = CharField(
        verbose_name='ФИО',
        max_length=256
    )

    phone = CharField(
        verbose_name='Номер телефона',
        max_length=20
    )

    email = EmailField(
        verbose_name='Email'
    )

    age = PositiveSmallIntegerField(
        verbose_name='Возраст'
    )

    languages = CharField(
        verbose_name='Языки',
        max_length=512
    )

    town = CharField(
        verbose_name='Город',
        max_length=128
    )

    website = CharField(
        verbose_name='Вебсайт',
        max_length=256
    )

    about = TextField(
        verbose_name='Подробнее'
    )

    class Meta:

        verbose_name = 'Запрос моделя'
        verbose_name_plural = 'Запросы моделям'