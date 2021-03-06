# Generated by Django 3.1.4 on 2021-02-19 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoModelForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=255, verbose_name='ユーザID')),
            ],
        ),
        migrations.CreateModel(
            name='SecondInfoModelForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wordID', models.CharField(max_length=255, verbose_name='単語ID')),
                ('userID', models.CharField(max_length=255, verbose_name='ユーザID')),
                ('eng', models.CharField(max_length=255, verbose_name='英語')),
                ('jan', models.CharField(max_length=255, verbose_name='日本語')),
            ],
        ),
        migrations.CreateModel(
            name='ThirdInfoModelForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=255, verbose_name='ユーザID')),
                ('name', models.CharField(max_length=255, verbose_name='名前')),
                ('password', models.CharField(max_length=255, verbose_name='パスワード')),
            ],
        ),
    ]
