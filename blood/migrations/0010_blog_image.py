# Generated by Django 5.0.6 on 2024-11-22 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0009_category_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=0, upload_to='blog_images/'),
            preserve_default=False,
        ),
    ]