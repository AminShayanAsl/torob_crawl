# Generated by Django 2.2.10 on 2021-06-12 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_delete_test_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i', models.IntegerField()),
                ('j', models.IntegerField()),
                ('product_id', models.IntegerField()),
            ],
        ),
    ]