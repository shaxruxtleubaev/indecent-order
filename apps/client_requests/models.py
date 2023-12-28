from django.db.models import *

from apps.models.models import Models

class ClientRequest(Model):

    name = CharField(
        verbose_name='ФИО',
        max_length=256
    )

    phone = CharField(
        verbose_name='Номер телефона',
        max_length=20
    )

    content = TextField(
        verbose_name='Контент'
    )

    model_id = ForeignKey(
        Models,
        verbose_name='ID моделя',
        on_delete=CASCADE,
        blank=True,
        null=True
    )

    class Meta:

        verbose_name = 'Запрос клиента'
        verbose_name_plural = 'Запросы клиентов'