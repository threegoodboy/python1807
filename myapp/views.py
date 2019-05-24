from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.urls import reverse

from myapp.cache import get_code


from myapp.models import Users, Investment, Relation

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
                return redirect(reverse('myapp:main'),username=username)
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
        code=request.POST.get('code')
        code2=get_code(str(phone))
        try:
            Users.objects.get(username=username)
            request.session['error_message'] = '用户名已存在'
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
                        user.password = password
                        user.phone = phone
                        user.code = code
                        user.save()
                        return redirect(reverse('myapp:login'))



            except:
                errornone={'Noneerror':'验证码已过期'}
                return render(request,'register.html',locals())







def loginout(request):
    request.session.flush()
    return redirect(reverse('myapp:index'))

def user_invest(request):
    return render(request,"invest.html")

def user_problem(request):
    return render(request,"problem.html")

def user_borrow(request):
    return render(request,"borrow.html")

def user_noticelist(request):
    return render(request,"noticelist.html")




