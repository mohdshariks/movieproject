# Generated by Django 4.1.5 on 2023-03-16 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0003_rename_img_movies_imgg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='imgg',
            new_name='img',
        ),
    ]
