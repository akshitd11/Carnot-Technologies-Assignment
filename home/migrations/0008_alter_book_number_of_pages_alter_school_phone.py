# Generated by Django 4.0.5 on 2022-06-12 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_school_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='number_of_Pages',
            field=models.CharField(max_length=122),
        ),
        migrations.AlterField(
            model_name='school',
            name='phone',
            field=models.CharField(max_length=122),
        ),
    ]
