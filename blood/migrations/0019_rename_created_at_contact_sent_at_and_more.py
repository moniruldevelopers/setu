# Generated by Django 5.0.6 on 2024-11-23 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0018_contact_delete_bloodrequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='created_at',
            new_name='sent_at',
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=200),
        ),
    ]
