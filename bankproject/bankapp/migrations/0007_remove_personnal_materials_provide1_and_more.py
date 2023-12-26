# Generated by Django 4.2.8 on 2023-12-25 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0006_remove_personnal_materials_provide_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personnal',
            name='materials_provide1',
        ),
        migrations.RemoveField(
            model_name='personnal',
            name='materials_provide2',
        ),
        migrations.RemoveField(
            model_name='personnal',
            name='materials_provide3',
        ),
        migrations.AddField(
            model_name='personnal',
            name='materials_provide',
            field=models.ManyToManyField(to='bankapp.material'),
        ),
    ]
