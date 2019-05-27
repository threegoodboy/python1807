from django.urls import path

from myapp.api import get_onecode
from myapp.views import *

app_name = 'myapp'

urlpatterns = [

    path('index/', user_index, name="index"),  # 首页
    path('login/', user_login, name="login"),  # 登录
    path('register/', user_register, name='register'),  # 注册
    path('problem/', user_problem, name='problem'),  # 常见问题
    path("borrow/", user_borrow, name='borrow'),  # 我要借款
    path("noticelist/", user_noticelist, name='noticelist'),  # 新手指引
    # path('invest/<pagenum>/', user_invest, name='invests'),  # 我要投资
    path('invest/', user_invest, name='invest'),  # 我要投资
    path('mycode/', get_onecode, name='code'),
    path('det/', detial, name='det'),
    path('inv_ajax/',invest_ajax,name='inv'),
    path('shouup/',shou_up,name='show'),
    path('timeup/',time_up,name='time'),
    path('dateup/',date_up,name='date'),
    path('page/',page_agax,name='pag'),
    path('detail/<id>/',user_detail,name='det'),
    path('touzi/<t_money>/<inv>/',touzi,name='tou')
]
