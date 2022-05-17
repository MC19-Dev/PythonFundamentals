# Generated by Django 4.0.4 on 2022-05-16 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_alter_action_contract_alter_contract_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='contract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='main.contract'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portofolios', to=settings.AUTH_USER_MODEL),
        ),
    ]
