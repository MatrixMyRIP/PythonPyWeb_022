# Generated by Django 4.2.5 on 2024-10-09 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.SlugField()),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('м', 'мужской'), ('ж', 'мужской')], max_length=1)),
                ('self_esteem', models.DecimalField(decimal_places=1, max_digits=2)),
                ('phone_number', models.CharField(max_length=12)),
                ('city', models.CharField(max_length=12)),
                ('bio', models.TextField()),
                ('age', models.IntegerField(editable=False, null=True)),
                ('date_birth', models.DateField()),
                ('status_rule', models.BooleanField()),
                ('image', models.ImageField(upload_to='foto_profile')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
