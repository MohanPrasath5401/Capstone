# Generated by Django 4.1.2 on 2022-11-29 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0006_profile2_remove_profile1_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('skills', models.TextField()),
                ('experience', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('skills', models.TextField()),
                ('experience', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Profile2',
        ),
    ]