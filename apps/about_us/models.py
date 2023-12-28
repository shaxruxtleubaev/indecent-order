from django.db.models import *

class Advantages(Model):

    title = CharField(
        verbose_name='Название',
        max_length=256
    )

    description = TextField(
        verbose_name='Описание'
    )

    image = ImageField(
        verbose_name='Фото',
        upload_to='about_us/advantages/'
    )

    def __str__(self):
        return f'{self.title}'
    
    class Meta:

        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'

class About_us(Model):

    years = PositiveSmallIntegerField(
        verbose_name='Годы'
    )

    models = IntegerField()

    clients = PositiveIntegerField(
        verbose_name='Клиенты'
    )
    
    advantages = ForeignKey(
        Advantages,
        verbose_name='Преимущества',
        on_delete=CASCADE
    )

    class Meta:

        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'