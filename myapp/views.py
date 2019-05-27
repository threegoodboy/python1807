import math
import os
import random
import uuid
import pytz
from django.core.paginator import Paginator
from django.db import connection
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect
from django.urls import reverse


from myapp.address_city import *
from myapp.cache import get_code
from myapp.models import *
import time
import datetime
from myapp.time_limit import tm_li
from myapp.cache import get_code

from myapp.models import Users, Investment, Relation

from myapp.myhelp.query_true import decide


def user_index(request):
    time_now = datetime.datetime.now().replace(tzinfo=pytz.timezone('UTC'))
    all_invests = Investment.objects.all()
    # print(all_invests)
    for invest in all_invests:
        # a = Investment.objects.filter(id=invest.id)
        # b = round(a.first().receive_money/a.first().project_money*100,1)
        # a.update(scale=b)
        # a = Investment.objects.filter(id=invest.id)
        # a.update(done=random.choice([1,0]))
        # a = Investment.objects.filter(id = invest.id)
        # a.update(date_los = (invest.time_limit - time_now).days)
        if invest.time_limit <= time_now:
            Investment.objects.get(id=invest.id).delete()
        # if tm_li(invest.id):
        #     Investment.objects.get(id = invest.id).delete()
    inv_num = Users.objects.filter(invest_money__gt=0).count()
    loan_num = Users.objects.filter(loan_money__gt=0).count()
    user_num = Users.objects.count()
    mark_info1 = Investment.objects.get(id=1)
    mark_info2 = Investment.objects.get(id=2)
    all_make = Investment.objects.all()
    now = datetime.datetime.now()
    # date_limit = (now - datetime.timedelta(days=7)).replace(tzinfo=pytz.timezone('UTC'))
    # gt7 = Investment.objects.filter(make_time__lte=date_limit)
    gt7 = Investment.objects.filter(date_los__lte=500)

    print(gt7)
    user_dict = {}
    for gtob in gt7:
        user_money = gtob.one_invest_money
        user_id = Relation.objects.filter(user=gtob).first().id
        for key, value in user_dict.items():
            if key == user_id:
                user_dict[user_id] = value + user_money
            else:
                user_dict[user_id] = user_money
    list1 = user_dict.items()
    list2 = sorted(list1, key=lambda x: x[1], reverse=True)
    user_max5 = []
    user_max5_dict = {}
    for tup1 in list2[:5]:
        id = user_max5.append(tup1[0])
        user_max5_dict[id] = [Users.objects.get(id=id), user_dict[id]]
    # user_num = 1000
    # print(user_num)
    a=Q(id__gte=10)
    b = Q(id__lte=14)
    c = Investment.objects.filter(a&b)
    print(user_max5_dict)
    data = {
        'inv_unm': inv_num,
        'loan_umn': loan_num,
        'user_unm': user_num,
        'ranking': user_max5_dict,
        'mark_info1':mark_info1,
        'mark_info2':mark_info2,
        'c':c
    }
    return render(request, "index.html",data)


def user_login(request):
    if request.method == "GET":
        error_message = request.session.get('error_message')
        user_error = request.session.get('user_error')
        data = {}
        if error_message:
            del request.session['error_message']
            data['error_message'] = error_message
        elif user_error:
            del request.session['user_error']
            data['user_error'] = user_error
        return render(request, 'login.html', data)
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = Users.objects.filter(username=username)
        # print(username,"ss"*50)
        if users.exists():
            user = users.first()
            request.session['id'] = user.id
            if check_password(password, user.password):
                request.session['username'] = user.username
                return redirect(reverse('myapp:index'))
            else:
                request.session['error_message'] = "密码错误！"
                return redirect(reverse('myapp:login'))
        else:
            request.session['user_error'] = "该用户不存在！"
            return redirect(reverse('myapp:login'))


def user_register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password', None)
        newpassword = request.POST.get('newpassword')
        phone = request.POST.get('phone')
        code = request.POST.get('code')
        code2 = get_code(str(phone))
        try:
            Users.objects.get(username=username)
            request.session['error_message'] = '用户名已存在'
            msg = {'usernameerror': '用户名已存在'}
            return render(request, 'register.html', locals())

        except:
            try:
                if code != code2.decode():
                    errorcode = {'codeerror': '验证码不正确'}
                    return render(request, 'register.html', locals())
                else:

                    user = Users()
                    user.username = username
                    user.password = make_password(password)
                    user.phone = phone
                    user.code = code
                    user.save()
                    return redirect(reverse('myapp:login'))



            except:
                errornone = {'Noneerror': '验证码已过期'}
                return render(request, 'register.html', locals())


def loginout(request):
    request.session.flush()
    return redirect(reverse('myapp:index'))


def invest_ajax(request):
    all= " min_money>=0"
    all1 = " and max_money>=0"
    lt1 = "  and date_los<30"
    lt2_3 = '  and date_los>60 and date_los<=90'
    lt4_6 = '  and date_los>120 and date_los<=180'
    lt7_12 = '  and date_los>210 and date_los<=360'
    # all = Investment.objects.all()
    # lt1 = Investment.objects.filter(date_los__lt=30)
    # a1 = Q(date_los__lte=90)
    # a2 = Q(date_los__gt=60)
    # lt2_3 = Investment.objects.filter(a1 & a2)
    # a3 = Q(date_los__lte=180)
    # a4 = Q(date_los__gt=120)
    # lt4_6 = Investment.objects.filter(a3 & a4)
    # a5 = Q(date_los__lte=360)
    # a6 = Q(date_los__gt=210)
    # lt7_12 = Investment.objects.filter(a5 & a6)
    l1 = [all1,lt1, lt2_3, lt4_6, lt7_12]

    all_loan = ' and receive_money>0'
    now_loan = ' and receive_money>=0 and done=0'
    suc_loan = ' and receive_money>0'
    done_loan = ' and done=1'
    # all_loan = Investment.objects.filter(receive_money__gt=0)
    # now_loan = Investment.objects.filter(receive_money__gte=0) & Investment.objects.filter(done=1)
    # user_id = request.session.get('id')
    # # suc_loan = Users.objects.get(id=user_id).Relation_set.all()
    # suc_loan = all
    # done_loan = Investment.objects.filter(done=1)
    l2 = [all1,all_loan, now_loan, suc_loan, done_loan]

    profit_10 = ' and year_money<10'
    profit_15 = ' and year_money>=10 and year_money<15'
    profit_20 = ' and year_money>=15 and year_money<20'
    profit_30 = ' and year_money>=20 and year_money<30'
    #
    # profit_10 = Investment.objects.filter(year_money__lt=10)
    #
    # q1 = Q(year_money__gte=10)
    # q2 = Q(year_money__lte=15)
    # profit_15 = Investment.objects.filter(q1 & q2)
    #
    # q3 = Q(year_money__gte=15)
    # q4 = Q(year_money__lte=20)
    # profit_20 = Investment.objects.filter(q3 & q4)
    #
    # q5 = Q(year_money__gte=20)
    # q6 = Q(year_money__lte=30)
    # profit_30 = Investment.objects.filter(q5 & q6)
    l3 = [all1,profit_10, profit_15, profit_20,profit_30]

    credit_label = " and label='信用'"
    mortgage_label = " and label='贷款'"
    # credit_label = Investment.objects.filter(label='信用')
    # mortgage_label = Investment.objects.filter(label='贷款')
    l4 = [all1,credit_label, mortgage_label]
    lists = request.session.get('inv_lists')
    a = int(request.POST.get('a'))
    b = int(request.POST.get('b'))

    lists[a] = b-1
    l_all = [l1, l2, l3, l4]
    show = all
    for index, value in enumerate(lists):
        if value > 10:
            show = show
        else:
            show += l_all[index][value]
    sql = "select * from investment where" +show
    request.session['sql'] = sql
    show_num = Investment.objects.raw('select * from (%s) investment LIMIT 0, 6' %(sql,))
    # show_num = all
    # for index, value in enumerate(lists):
    #     if value > 10:
    #         show_num = show_num
    #     else:
    #         show_num = show_num & (l_all[index][value])
    aa = []
    for i in show_num:
        if i.done == 1:
            done_name = '已完成'
        else:
            done_name = '立即支付'
        aa.append([i.label,i.markname,i.year_money,i.date_los,i.security_system,i.project_money,i.scale,done_name,i.id])
    request.session['inv_lists'] = lists
    # request.session['aa'] = show_num

    page = int(request.GET.get('page', 1))
    sql = request.session.get('sql', None)
    sql = "select count(*) from (%s) investment"%(sql,)
    c = connection.cursor()
    c.execute(sql)
    total = c.fetchone()[0]
    print(total)
    total_pages = math.ceil(total / 6)
    # page_range = range(1,total_pages)
    page_range = range(page-2 if page-2 >= 1 else 1,
                       page+5 if page + 5 <= total_pages else total_pages)

    data={
        'aa':aa,
        'page_range':list(page_range),
    }

    print(show_num)
    return JsonResponse(data)

def page_agax(request):
    sql = request.session.get('sql')
    page = int(request.POST.get('ind'))
    print(page,'00000000000000000000')


    c = connection.cursor()
    c.execute("select count(*) from (%s) investment"%(sql,))
    total = c.fetchone()[0]
    print(total)
    total_pages = math.ceil(total / 6)
    # page_range = range(1,total_pages)
    page_range = range(page-2 if page-2 >= 1 else 1,
                       page+3 if page + 3 <= total_pages else total_pages)

    # show_num = Investment.objects.raw('select * from (%s) investment LIMIT 0, 6' % (sql,))
    show_num = Investment.objects.raw('select * from (%s) investment LIMIT %s, %s' % (sql,(page - 1) * 6, 6))
    aa = []
    for i in show_num:
        if i.done == 1:
            done_name = '已完成'
        else:
            done_name = '立即支付'
        aa.append([i.label,i.markname,i.year_money,i.date_los,i.security_system,i.project_money,i.scale,done_name,i.id])

    data={
       'aa':aa,
       'page_range': list(page_range),
    }

    return JsonResponse(data)


def shou_up(request):
    sq = request.session.get('sql')
    sql = "select * from (%s) investment order by year_money"%(sq)
    request.session['sql']=sql #1
    show_num = Investment.objects.raw('select * from (%s) investment LIMIT 0, 6' % (sql,))
    # show_num = Investment.objects.raw(sql+' order by year_money')
    aa = []
    for i in show_num:
        if i.done == 1:
            done_name = '已完成'
        else:
            done_name = '立即支付'
        aa.append([i.label,i.markname,i.year_money,i.date_los,i.security_system,i.project_money,i.scale,done_name,i.id])

    data={
       'aa':aa
    }

    return JsonResponse(data)


def time_up(request):
    sq = request.session.get('sql')
    sql = "select * from (%s) investment order by make_time" % (sq)
    request.session['sql']=sql #1
    show_num = Investment.objects.raw('select * from (%s) investment LIMIT 0, 6' % (sql,))
    aa = []
    for i in show_num:
        if i.done == 1:
            done_name = '已完成'
        else:
            done_name = '立即支付'
        aa.append([i.label,i.markname,i.year_money,i.date_los,i.security_system,i.project_money,i.scale,done_name,i.id])

    data={
       'aa':aa
    }

    return JsonResponse(data)

def date_up(request):
    sq = request.session.get('sql')
    sql = "select * from (%s) investment order by date_los" % (sq)
    request.session['sql']=sql #1
    show_num = Investment.objects.raw('select * from (%s) investment LIMIT 0, 6' %(sql,))
    aa = []
    for i in show_num:
        if i.done == 1:
            done_name = '已完成'
        else:
            done_name = '立即支付'
        aa.append([i.label,i.markname,i.year_money,i.date_los,i.security_system,i.project_money,i.scale,done_name,i.id])

    data={
       'aa':aa
    }

    return JsonResponse(data)


# def touzi(request):
#     user_id = request.session.git('id')
#     data1 = request.GET.get('data_')
#     user = Users.objects.get(id = user_id)
#     inv = Investment.objects.get(markname=inv_name)
#     f = Relation.objects.create(one_invest_money=)
#     f.save()
#     data={}
#     return JisonResponse(data)

# def user_invest(request, pagenum=1):
#     inv_lists=[100,100,100,100]
#     request.session['inv_lists'] = inv_lists
#     if request.session.get('aa'):
#         show_num_is = request.session.get('aa')
#     else:
#         show_num_is = Investment.objects.all()
#     page_size = 6
#     paginator = Paginator(show_num_is, page_size)
#     page = paginator.page(pagenum)
#     data = {
#         'page': page,
#         'paginator': paginator,
#         'show_num_is': show_num_is
#     }
#     return render(request, 'invest.html', data)
def user_invest(request):
    inv_lists=[100,100,100,100]
    request.session['inv_lists'] = inv_lists
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('size', 6))

    total_pages = request.session.get('total_pages', None)
    sql = request.session.get('sql',None)
    if sql is None:
        sql = "select * from investment"
        request.session['sql']=sql
    sql = "select count(*) from (%s) investment"%(sql,)
    # if total_pages is None:
    #     c = connection.cursor()
    #     c.execute(sql)
    #     total = c.fetchone()[0]
    #     total_pages = math.ceil(total / page_size)
    #     # request.session['total_pages'] = total_pages
    #     # print('totalpages: ', total_pages)
    page_range = range(1,6)
    # print(page_range,"*"*60)
    # request.session['page_range']=page_range
    invests = Investment.objects.raw('select * from investment LIMIT %s, %s' %((page-1)*6, 6))
    return render(request, 'invest.html', locals())

def page_ajax(request):
    page = request.GET.get('page',1)
    sql = request.session.get('sql')
    show_num = Investment.objects.raw('select * from (%s)investment LIMIT %s, %s' %(sql,(page-1)*6, 6))
    aa = []
    for i in show_num:
        if i.done == 1:
            done_name = '已完成'
        else:
            done_name = '立即支付'
        aa.append([i.label,i.markname,i.year_money,i.date_los,i.security_system,i.project_money,i.scale,done_name,i.id])

    data={
       'aa':aa
    }

    return JsonResponse(data)



def detial(request):
    # det = request.GET.get('det')
    # inv_det = Investment.objects.get(id=det)

    return render(request, 'detail.html')


def detial_ajax(request):
    inv_m = request.GET.get('inv_m')
    user = request.session.get('id')
    inv_det = Investment.objects.get(id=inv_m[0])
    inv_det.first().receive_money -= inv_m[1]
    Relation.objects.create(user=user, investment=inv_det, one_invest_money=inv_m[1])
    data = {}
    return JsonResponse(data)


def chat_ajax(request):
    pass


def address_ajax(request):
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']

    data = ip_print_AddrInfo(ip)

    return JsonResponse(data)


def up_file(request):
    if request.method == "POST":
        file = request.files.get('file')
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_name = uuid.uuid4().hex + os.path.splitext(file.name)[-1]
        file_path = os.path.join(base_dir, "imgs/" + file_name)
        request.session['photo'] = file_path
        with open(file_path, 'w') as f:
            for chunk in file.chunks():
                f.write(chunk)
        data = {
            'status': 200,
            'path': file_path
        }
        return JsonResponse(data)
    if request.method == 'GET':
        if request.session.get("id"):
            photo_path = request.session.get('photo')
            data1 = {
                "photo": photo_path
            }
    return JsonResponse(data1)


def user_check(request):
    user_id = request.session.get('id')
    user = Users.objects.get(id=user_id)
    check_user = user.check_user
    if check_user.time_old is None:
        check_user.this_score = 1
        check_user.all_score = 1
        check_user.save()
        data = {
            'msg': '签到成功'
        }
        return JsonResponse(data)
    else:
        today = datetime.date.today()
        if today - check_user.time_old == 0:
            data = {
                'msg': '已经签到，请勿再次操作'
            }
            return JsonResponse(data)
        elif today - check_user.time_old == 1:
            check_user.this_score += check_user.this_score
            check_user.all_score += check_user.this_score
            check_user.save()
            data = {
                'msg': '签到成功'
            }
            return JsonResponse(data)
        else:
            check_user.this_score += 1
            check_user.all_score += check_user.this_score
            check_user.save()
            data = {
                'msg': '签到成功'
            }
            return JsonResponse(data)


def user_main(request):
    user_id = request.session.get('id')
    user = Users.objects.get(id=user_id)
    if user.check_user.all_score < 50 and user.check_user.all_score > 30:
        user.vip_level = '白银'
        user.save()
    if user.check_user.all_score > 90:
        user.vip_level = '黄金'
        user.save()
    data = {
        'user': user
    }
    return JsonResponse(data)


def user_problem(request):
    return render(request, "problem.html")


def user_borrow(request):
    return render(request, "borrow.html")


def user_noticelist(request):
    return render(request, "noticelist.html")

def user_detail(request,id):
    if request.method == "GET":
        inv = Investment.objects.get(id=id)
        a = random.choice(['12','24','48','36'])
        invpro = inv.project_money/10000
        data ={
            'inv':inv,
            'a':a,
            'invpro':invpro
        }
        return render(request,'detail.html',data)
    if request.method == "POST":
        t_money = request.POST.get('touzi')
        inv = Investment.objects.get(id=id)
        data={
            't_money':t_money,
            'inv':inv
        }
        return redirect(reverse('myapp:tou',args=(t_money,inv)))



def touzi(request,t_money,inv):
    id = request.session.get('id')
    user = Users.objects.get(id = id)
    user.use_money += int(t_money)
    user.invest_money -= int(t_money)
    user.save()
    data={
        'user':user,
        'inv':inv
    }
    return render(request,'touzi.html',data)
