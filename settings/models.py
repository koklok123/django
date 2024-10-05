from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок сайта'
    )
    description = models.TextField(
        verbose_name='Описание сайта'
    )
    logo = models.ImageField(
        upload_to='logo_image/'
    )
    phone_number = models.IntegerField(
        verbose_name='Номер телефона'
    )
    email = models.EmailField(
        verbose_name="Укажите почту"
    )
    instagram = models.URLField(
        verbose_name="Ссылка на instagram"
    )
    
    
class Galery(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    image = models.ImageField(
        upload_to='galery/'
    )
    description = models.TextField(
        verbose_name='Описание фото'
    )