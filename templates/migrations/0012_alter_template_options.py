# Generated by Django 3.2.6 on 2021-08-28 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0011_alter_like_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='template',
            options={'ordering': ('-created_at',)},
        ),
    ]
