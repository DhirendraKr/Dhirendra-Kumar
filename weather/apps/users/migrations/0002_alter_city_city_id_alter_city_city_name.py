# Generated by Django 4.0.3 on 2022-03-14 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city_id',
            field=models.AutoField(db_column='city_id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='city',
            name='city_name',
            field=models.CharField(db_column='city_name', max_length=60),
        ),
    ]
