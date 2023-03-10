# Generated by Django 4.1.2 on 2022-11-17 03:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('latitude', models.DecimalField(decimal_places=15, max_digits=17)),
                ('longitude', models.DecimalField(decimal_places=15, max_digits=17)),
                ('postal_code', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator('^[A-Za-z]\\d[A-Za-z][ -]?\\d[A-Za-z]\\d$', 'Invalid postal code')])),
                ('phone_num', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^(\\+\\d{1,2}\\s)?\\(?\\d{3}\\)?[\\s.-]\\d{3}[\\s.-]\\d{4}$', 'Invalid phone number')])),
            ],
        ),
        migrations.CreateModel(
            name='StudioImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='studios.studio')),
            ],
            options={
                'verbose_name': "Studio's Images",
                'verbose_name_plural': "Studio's Images",
            },
        ),
    ]
