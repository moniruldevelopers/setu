# Generated by Django 5.0.6 on 2024-11-23 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0015_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
