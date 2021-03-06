# Generated by Django 3.0 on 2019-12-05 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='photos/products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to='photos/products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to='photos/products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo_main',
            field=models.ImageField(upload_to='photos/products/%Y/%m/%d'),
        ),
    ]
