# Generated by Django 3.2.12 on 2024-02-18 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tags',
        ),
    ]
