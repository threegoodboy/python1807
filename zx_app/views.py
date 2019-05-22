from django.db.models import Q
from django.shortcuts import render
# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect
from django.urls import reverse

from zx_app.models import *
import time

from zx_app.time_limit import tm_li


def main_index(request):
    all_invests = Investment.objects.all()
    for invest in all_invests:
        if tm_li(invest.id):
            Investment.objects.get(id = invest.id).delete()
    inv_num = Users.objects.filter(invest_money__gt=0).count()
    loan_num = Users.objects.filter(loan_money__gt=0).count()
    user_num = Users.objects.count()
    # mark_info1 = Investment.objects.get(id=1)
    # mark_info2 = Investment.objects.get(id=2)
    all_make = Investment.objects.all()
    gt7 = Investment.objects.filter(make_time__lte=2019-5-25)
    user_dict = {}
    for gtob in gt7:
        user_money = gtob.one_invest_money
        user_id = Relation.objects.filter(user=gtob).id
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
        # 'mark_info1':mark_info1,
        # 'mark_info2':mark_info2,
    }
    return render(request,'index.html')

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        invcode = request.POST.get('invcode')
        invest_money = request.POST.get('invest_money')
        loan_money = request.POST.get('loan_money')
        try:
            Users.objects.get(username=username)
            request.session['error_message'] = '用户名已存在'
            return render(request,'register.html')
        except:
            user = Users()
            user.username = username
            user.password = make_password(password)
            user.phone = phone
            user.invcode = invcode
            user.invest_money = invest_money
            user.loan_money = loan_money
            user.save()
            return redirect(reverse('zx:login'))
def login(request):
    if request.method == "GET":
        error_message = request.session.get('error_message')
        data = {}
        if error_message:
            del request.session['error_message']
            data['error_message'] = error_message
        return render(request,'login.html',data)
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        users = Users.objects.filter(username=username)
        if users.exists():
            user = users.first()
            request.session['user_id'] = user.id
            if check_password(password,user.password):
                return redirect(reverse('zx:main'),username=username)
            else:
                request.session['error_message'] = "密码错误！"
                return redirect(reverse('zx:login'))
        else:
            request.session['error_message'] = "该用户不存在！"
            return redirect(reverse('zx:login'))

def loginout(request):
    request.session.flush()
    return redirect(reverse('zx:main'))

