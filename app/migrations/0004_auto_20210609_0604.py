# Generated by Django 2.2.10 on 2021-06-09 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210609_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price_list',
            name='product_description',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='price_list',
            name='remark',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='source_product',
            name='name',
            field=models.CharField(max_length=512),
        ),
    ]