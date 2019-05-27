import sys

import pymysql

sys.path.append('.')
import random
from datetime import datetime

from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.urls import reverse

from myapp.cache import get_code


from myapp.models import Users, Investment, Relation
from myapp.myhelp.http import render_json

from myapp.myhelp.query_true import decide
from myapp.time_limit import tm_li


def user_index(request):
    all_invests = Investment.objects.all()
    for invest in all_invests:
        if tm_li(invest.id):
            Investment.objects.get(id = invest.id).delete()
    inv_num = Users.objects.filter(invest_money__gt=0).count()
    loan_num = Users.objects.filter(loan_money__gt=0).count()
    user_num = Users.objects.count()
    mark_info1 = Investment.objects.get(id=1)
    mark_info2 = Investment.objects.get(id=2)
    all_make = Investment.objects.all()
    gt7 = Investment.objects.filter(make_time__lte=2019-5-25)
    user_dict = {}
    for gtob in gt7:
        user_money = gtob.one_invest_money
        user_id = Relation.objects.filter(user=gtob).first().id
        for key,value in user_dict.items():
            if key == user_id:
                user_dict[user_id] = value + user_money
            else:
                user_dict[user_id] = user_money
    list1 = user_dict.items()
    list2 = sorted(list1,key=lambda x:x[1],reverse=True)
    user_max5 = []
    user_max5_dict = {}
    for tup1 in list2[:5]:
        id = user_max5.append(tup1[0])
        user_max5_dict[id] = [Users.objects.get(id=id),user_dict[id]]
    data = {
        'inv-unm': inv_num,
        'loan_umn': loan_num,
        'user_unm': user_num,
        'ranking': user_max5_dict,
        'mark_info1':mark_info1,
        'mark_info2':mark_info2,
    }
    return render(request,"index.html")


def user_login(request):
    if request.method == "GET":
        error_message = request.session.get('error_message')
        user_error=request.session.get('user_error')
        data = {}
        if error_message:
            del request.session['error_message']
            data['error_message'] = error_message
        elif user_error:
            del request.session['user_error']
            data['user_error']=user_error
        return render(request,'login.html',data)
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = Users.objects.filter(username=username)
        if users.exists():
            user = users.first()
            request.session['user_id'] = user.id
            if check_password(password,user.password):
                request.session['username']=user.username
                return redirect(reverse('myapp:invest'))
            else:
                request.session['error_message'] = "密码错误！"
                return redirect(reverse('myapp:login'))
        else:
            request.session['user_error'] = "该用户不存在！"
            return redirect(reverse('myapp:login'))


def user_register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password',None)
        newpassword=request.POST.get('newpassword')
        phone = request.POST.get('phone')
        yh=request.POST.get('yh')
        code=request.POST.get('code')
        code2=get_code(str(phone))
        try:
            Users.objects.get(username=username)

            msg={'usernameerror':'用户名已存在'}
            return render(request, 'register.html', locals())

        except:
            try:
                if code !=code2.decode():
                        errorcode={'codeerror':'验证码不正确'}
                        return render(request,'register.html',locals())
                else:

                        user = Users()
                        user.username = username
                        user.password = make_password(password)
                        user.phone = phone
                        user.code = code
                        user.invcode = yh
                        if not password.isdigit():
                            user.level='高'
                        else:
                            user.level='低'
                        print(123,'+++++++')
                        user.save()
                        print(1234,'++++++++++++')

                        return redirect(reverse('myapp:login'))



            except:
                errornone={'Noneerror':'验证码已过期'}
                return render(request,'register.html',locals())






def user_msg(request):
    if request.method=='GET':
        username=request.session.get('username',None)
        if username== None:
            return redirect(reverse('myapp:login'))
        users=Users.objects.filter(username=username)

        for user in users:
            myname=user.username
            myid=user.id
            mylevel=user.level
            mytime=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            mynum=user.number

            money=user.use_money
            if money >= 3000:
                img="../../static/grzl_files/vip4.png"
            elif money >= 20000:
                img="../../static/grzl_files/vip3.png"
            elif money >= 10000:
                img="../../static/grzl_files/vip2.png"
            elif money >=0:
                url="../../static/grzl_files/vip1.png"


        return render(request,'grzl.html',locals())

def have_pymysql():
    conn=pymysql.connect(host='localhost',port=3306,user='root',password='z979320182',charset='utf8',db='myproject')
    cursor=conn.cursor()
    return cursor,conn

#充值页面

def user_cz(request):
    if request.method=='GET':
        phone=request.session.get('phone')
        none=request.session.get('buNone')
        dif=request.session.get('buyizhi')
        dict1={}
        if phone:

            del request.session['phone']
            dict1['myphone']=phone
        if none:
            del request.session['buNone']
            dict1['mynone']=none
        if dif:
            del request.session['buyizhi']
            dict1['yizhi']=dif

        return render(request,'cz.html',dict1)
    if request.method=='POST':

        username = request.session.get('username', None)
        if username == None:
            return redirect(reverse('myapp:login'))
        users=Users.objects.filter(username=username)
        user=users.first()
        phone=request.POST.get('pay_user_repeat',None)
        phone2 = request.POST.get('pay_user_repeat2',None)
        if user.phone!=phone:
            request.session['phone']='账号不存在'

            return redirect(reverse('myapp:cz'))
        if phone==None or phone2==None:
            request.session['buNone']='用户名或重输入不能为空'
            return redirect(reverse('myapp:cz'))
        if phone !=phone2:
            request.session['buyizhi']='两次输入不一致'
            return redirect(reverse('myapp:cz'))

        allmoney=0
        money=request.POST.get("pay_money")
        newmoney = request.POST.get("mymoney")
        allmoney=money+newmoney

        mymoney=int(allmoney)+user.invest_money

        cursor,conn=have_pymysql()
        sql='update users set invest_money="%s" where username= "%s"'%(mymoney,user.username)
        cursor.execute(sql)
        conn.commit()
        conn.close()
        cursor.close()

        return redirect(reverse('myapp:msg'))


#投资页面
def user_invest(request):
    if request.method=='GET':
        dict={}
        username=request.session.get('username',None)
        if username is not None:
            dict['username']=username
            return render(request,"invest.html",dict)
        else:
            return render(request,"invest.html")


#删除session信息
def del_session(request):
    del request.session['username']
    return redirect(reverse('myapp:invest'))

#提现页面
def user_tx(request):
    return render(request,'tx.html')


def user_problem(request):
    return render(request,"problem.html")

def user_borrow(request):
    return render(request,"borrow.html")

def user_noticelist(request):
    return render(request,"noticelist.html")




