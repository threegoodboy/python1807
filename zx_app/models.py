from django.db import models

# Create your models here.

class Users(models.Model):

    username = models.CharField(max_length=120)
    password = models.CharField(max_length=150)
    phone = models.IntegerField()
    invcode = models.CharField(max_length=6)
    invest_money = models.IntegerField(default=0,null=True)
    loan_money = models.IntegerField(default=0,null=True)

    class Meta:
        db_table = 'users'

class Investment(models.Model):
    markname = models.CharField(max_length=20)
    min_money = models.IntegerField()
    max_money = models.IntegerField()
    receive_money = models.CharField(max_length=10)
    time_limit = models.CharField(max_length=10)
    year_money = models.CharField(max_length=10)
    label = models.CharField(max_length=5)
    make_time = models.TimeField()
    # userid = models.IntegerField()
    user = models.ManyToManyField(Users,through='Relation')
    class Meta:
        db_table = 'investment'

# class Loan(models.Model):
#     markname = models.CharField(max_length=20)
#     time_limit = models.CharField(max_length=10)
#     year_money = models.CharField(max_length=10)
#     all_money = models.IntegerField()
#     loan_time = models.TimeField()
#     loan_user = models.ManyToManyField(Users, through='Relation')
#     class Meta:
#         db_table = 'loan'

class Relation(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    one_invest_money = models.IntegerField(default=0)
    one_loan_money = models.IntegerField(default=0)
    class Meta:
        db_table='relation'
