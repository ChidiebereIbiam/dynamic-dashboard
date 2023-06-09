# Generated by Django 4.1.9 on 2023-05-21 23:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_basis', models.FloatField(default=100)),
                ('current_value', models.FloatField(default=100)),
                ('portfolio_return', models.FloatField(default=0.0)),
                ('user', djongo.models.fields.ArrayReferenceField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
