# Generated by Django 4.0.2 on 2022-05-17 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halalan2022', '0010_alter_user_birthday_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
