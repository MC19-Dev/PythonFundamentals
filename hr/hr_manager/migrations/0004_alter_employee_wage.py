# Generated by Django 4.0.4 on 2022-05-16 01:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_manager', '0003_alter_employer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='wage',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
