from django.db import models

# Create your models here.

class Users(models.Model):       #用户表

    username = models.CharField(max_length=20,verbose_name='用户名')    #用户名
    password = models.CharField(max_length=100,verbose_name='用户密码')    #用户密码
    invcode = models.CharField(max_length=50,verbose_name='银行卡号')        #银行卡
    phone = models.CharField(max_length=11,verbose_name='手机号')   #手机号
    invest_money = models.IntegerField(default=0,verbose_name='投资资金')  #用户资金
    level=models.CharField(max_length=10, default='低')    #安全等级
    loan_money = models.IntegerField(default=0,verbose_name='借款资金')     # 借款
    code = models.CharField(max_length=4,verbose_name='验证码')    #验证码
    number=models.CharField(max_length=30,default=0)    #用户积分
    use_money=models.IntegerField(default=0)  #用户已投资资金
    #验证码
    class Meta:
        db_table = 'users'
        verbose_name='用户模型'
        verbose_name_plural=verbose_name

class Investment(models.Model):
    markname = models.CharField(max_length=20,verbose_name='项目名字')   #项目名称
    min_money = models.IntegerField(verbose_name='最少投资资金')    #最少资金
    max_money = models.IntegerField(verbose_name='最大投资资金')       #最大资金
    receive_money = models.IntegerField(verbose_name='已投资资金')   #投资资金
    time_limit = models.DateTimeField(auto_now_add=True,verbose_name='项目到期时间')    #期限
    year_money = models.FloatField(verbose_name='年收益率')    #年收益
    label = models.CharField(max_length=5,verbose_name='标签')    # 标签名
    make_time = models.DateTimeField(auto_now=True,verbose_name='项目开始时间')    #项目开始时间
    project_money=models.IntegerField('项目总额度')  #项目总额
    security_system=models.CharField(max_length=30,verbose_name='保障机构')  #保障机构
    done=models.IntegerField(null=True,verbose_name='项目完成率')    #已完成占比
    date_los=models.IntegerField(null=True,verbose_name='项目剩余天数')  #剩余日期
    # userid = models.IntegerField()
    user = models.ManyToManyField(Users,through='Relation')
    class Meta:
        db_table = 'investment'
        verbose_name='项目模型'
        verbose_name_plural=verbose_name
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

