# Generated by Django 4.1.2 on 2022-11-29 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0005_updatepost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('skills', models.TextField()),
                ('education', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='profile1',
            name='user',
        ),
    ]