# Generated by Django 4.2.5 on 2024-10-09 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_train', '0004_alter_author_email_alter_author_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
    ]