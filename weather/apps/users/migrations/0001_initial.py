# Generated by Django 4.0.3 on 2022-03-14 19:24

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(db_column='atta_id', primary_key=True, serialize=False, verbose_name='id')),
                ('city_name', models.CharField(db_column='atta_file_name', max_length=255, verbose_name='filename')),
                ('is_default', models.BooleanField(db_column='is_default', default=False)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Citys',
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(db_column='username', max_length=254, unique=True)),
                ('email', models.CharField(db_column='email', max_length=254, unique=True)),
                ('user_create_date', models.DateTimeField(db_column='user_create_date', default=django.utils.timezone.now)),
                ('user_password_change_date', models.DateTimeField(db_column='user_password_change_date', null=True)),
                ('is_active', models.BooleanField(db_column='is_active', default=False)),
                ('is_staff', models.BooleanField(db_column='is_staff', default=False)),
                ('is_admin', models.BooleanField(db_column='is_admin', default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('username',), name='UK1_USER'),
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('email',), name='UK2_USER'),
        ),
    ]