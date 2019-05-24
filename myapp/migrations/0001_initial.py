# Generated by Django 2.2.1 on 2019-05-24 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('markname', models.CharField(max_length=20, verbose_name='项目名字')),
                ('min_money', models.IntegerField(verbose_name='最少投资资金')),
                ('max_money', models.IntegerField(verbose_name='最大投资资金')),
                ('receive_money', models.IntegerField(verbose_name='已投资资金')),
                ('time_limit', models.DateTimeField(auto_now_add=True, verbose_name='项目到期时间')),
                ('year_money', models.FloatField(verbose_name='年收益率')),
                ('label', models.CharField(max_length=5, verbose_name='标签')),
                ('make_time', models.DateTimeField(auto_now=True, verbose_name='项目开始时间')),
                ('project_money', models.IntegerField(verbose_name='项目总额度')),
                ('security_system', models.CharField(max_length=30, verbose_name='保障机构')),
                ('done', models.IntegerField(null=True, verbose_name='项目完成率')),
                ('date_los', models.IntegerField(null=True, verbose_name='项目剩余天数')),
            ],
            options={
                'verbose_name': '项目模型',
                'verbose_name_plural': '项目模型',
                'db_table': 'investment',
            },
        ),
        migrations.CreateModel(
            name='Pledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('borrow_money', models.IntegerField()),
                ('borrow_data', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('house_count', models.IntegerField()),
                ('price', models.IntegerField()),
                ('borrow', models.CharField(max_length=50)),
                ('borrow_describe', models.CharField(max_length=50)),
                ('borrow_case', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'pledge',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=30, verbose_name='用户密码')),
                ('invcode', models.CharField(max_length=4, verbose_name='邀请码')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('invest_money', models.IntegerField(default=0, verbose_name='投资资金')),
                ('loan_money', models.IntegerField(default=0, verbose_name='借款资金')),
                ('code', models.CharField(max_length=4, verbose_name='验证码')),
            ],
            options={
                'verbose_name': '用户模型',
                'verbose_name_plural': '用户模型',
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_invest_money', models.IntegerField(default=0)),
                ('one_loan_money', models.IntegerField(default=0)),
                ('investment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Investment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Users')),
            ],
            options={
                'db_table': 'relation',
            },
        ),
        migrations.AddField(
            model_name='investment',
            name='user',
            field=models.ManyToManyField(through='myapp.Relation', to='myapp.Users'),
        ),
    ]
