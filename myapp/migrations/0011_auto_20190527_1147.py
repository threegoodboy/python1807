# Generated by Django 2.2.1 on 2019-05-27 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_remove_users_user_yh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='invcode',
            field=models.CharField(default=0, max_length=4, verbose_name='银行卡号'),
        ),
    ]
