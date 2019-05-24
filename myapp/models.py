from django.db import models

# Create your models here.

class Users(models.Model):       #用户表

    username = models.CharField(max_length=20)    #用户名
    password = models.CharField(max_length=30)    #用户密码
    phone = models.IntegerField()                   #手机号
    invcode = models.CharField(max_length=6)        #邀请码
    invest_money = models.IntegerField(default=0)  #投资
    loan_money = models.IntegerField(default=0)     # 借款

    class Meta:
        db_table = 'users'

class Investment(models.Model):
    markname = models.CharField(max_length=20)   #项目名称
    min_money = models.IntegerField()    #最少资金
    max_money = models.IntegerField()       #最大资金
    receive_money = models.IntegerField()   #投资资金
    time_limit = models.DateTimeField(auto_now_add=True)    #期限
    year_money = models.FloatField()    #年收益   ***********
    label = models.CharField(max_length=5)    # 标签名
    make_time = models.TimeField()    #项目开始时间
    project_money=models.IntegerField()  #项目总额
    security_system=models.CharField(max_length=30)  #保障机构
    done=models.IntegerField()    #已完成
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
    one_invest_money = models.IntegerField(default=0)     #登录用户项目投资
    one_loan_money = models.IntegerField(default=0)     #登录用户借款资金
    class Meta:
        db_table='relation'

class Pledge(models.Model):
    name =models.CharField(max_length=10)
    borrow_money=models.IntegerField()  #借款金额
    borrow_data=models.IntegerField() #借款期限
    phone=models.IntegerField()  #手机号
    house_count=models.IntegerField()  #房屋数量
    price=models.IntegerField()  #房屋价值
    borrow=models.CharField(max_length=50) #借款用途
    borrow_describe=models.CharField(max_length=50) #借款描述
    borrow_case=models.CharField(max_length=50) #借款情况

    class Meta:
        db_table='pledge'

