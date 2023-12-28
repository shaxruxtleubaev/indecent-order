from django.db.models import *

class Languages(Model):

    language = CharField(
        verbose_name='Язык',
        max_length=128
    )

    def __str__(self):
        return f'{self.language}'
    
    class Meta:

        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

class Visa(Model):

    visa = CharField(
        verbose_name='Виза',
        max_length=256
    )

    def __str__(self):
        return f'{self.visa}'
    
    class Meta:

        verbose_name = 'Виза'
        verbose_name_plural = 'Виза'

class OtherImages(Model):

    image = ImageField(
        verbose_name='Фото',
        upload_to='models/other_images/'
    )

    def __str__(self):
        return f'{self.image.url}'
    
    class Meta:

        verbose_name = 'Другое фото'
        verbose_name_plural = 'Другие фото'

class Models(Model):

    name = CharField(
        verbose_name='ФИО',
        max_length=128
    )

    age = PositiveSmallIntegerField(
        verbose_name='Возраст'
    )

    bSize = IntegerField()

    languages = ManyToManyField(
        Languages,
        verbose_name='Языки',
    )

    visa = ManyToManyField(
        Visa,
        verbose_name='Виза',
    )

    interPassport = BooleanField(
        verbose_name='Загран паспорт'
    )

    mainImage = ImageField(
        verbose_name='Главное фото',
        upload_to='models/main_images/'
    )

    otherImages = ManyToManyField(
        OtherImages,
        verbose_name='Другие фото'
    )

    def __str__(self):
        return f'{self.id}'

    class Meta:

        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'