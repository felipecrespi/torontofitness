# Generated by Django 4.1.2 on 2022-11-18 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0011_alter_klass_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='klass',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='klass',
            constraint=models.UniqueConstraint(fields=('name', 'studio', 'day', 'start_time', 'end_time'), name='constraint'),
        ),
    ]