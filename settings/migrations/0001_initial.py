# Generated by Django 5.1.1 on 2024-10-05 12:41

from django.db import migrations, models
"""Первая миграция:

    Создается модель Settinng с полями для заголовка сайта, описания, логотипа, номера телефона, электронной поч """

# Generated by Django 5.1.1 on 2024-10-05 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settinng',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок сайта')),
                ('description', models.TextField(verbose_name='Описание сайта')),
                ('logo', models.ImageField(upload_to='logo_image/')),
                ('phone_number', models.IntegerField(verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Укажите почту')),
                ('instagram', models.URLField(verbose_name='Ссылка на instagram')),
            ],
        ),
    ]
# class Migration(migrations.Migration):

#     initial = True

#     dependencies = [
#     ]

#     operations = [
#         migrations.CreateModel(
#             name='Settinng',
#             fields=[
#                 ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
#                 ('name', models.TextField(verbose_name='Имя сотрудника')),
#                 ('position', models.TextField(verbose_name='Должность сотрудника')),
#                 ('photo', models.ImageField(upload_to='logo_image/')),
                
#             ],
#         ),
#     ]
    