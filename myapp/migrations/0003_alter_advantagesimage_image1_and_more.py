# Generated by Django 4.2.1 on 2023-05-16 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_advantagesimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advantagesimage',
            name='image1',
            field=models.ImageField(upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='advantagesimage',
            name='image2',
            field=models.ImageField(upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='advantagesimage',
            name='image3',
            field=models.ImageField(upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='advantagesimage',
            name='image4',
            field=models.ImageField(upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='advantagesimage',
            name='image5',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
