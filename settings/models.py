from django.db import models

# Create your models here.


class Setting(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Имя сотрудника'
    )
    position = models.CharField(
        max_length=100,
        verbose_name='Должность сотрудника'
    )
    photo = models.ImageField(
        upload_to='employee_photo/'
    )
    bio = models.TextField(
        verbose_name='Краткое описание или биография'
    )

class Galery(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    image = models.ImageField(
        upload_to='galery/'
    )
    description = models.TextField(
        verbose_name='Краткое содержание'
    )
