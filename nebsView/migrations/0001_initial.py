# Generated by Django 3.2.4 on 2021-06-06 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=50, verbose_name='Full name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email address')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone number')),
                ('message', models.TextField()),
            ],
        ),
    ]
