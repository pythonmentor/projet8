# Generated by Django 3.0.6 on 2020-06-22 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favoris', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='user_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_favoris', to=settings.AUTH_USER_MODEL),
        ),
    ]
