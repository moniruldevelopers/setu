# Generated by Django 5.0.6 on 2024-11-23 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0012_bloodrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]