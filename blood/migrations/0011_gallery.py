# Generated by Django 5.0.6 on 2024-11-22 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0010_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='gallery_images/')),
            ],
        ),
    ]
