from django.urls import path

from myapp.views import *

app_name='myapp'
urlpatterns = [
    path('index/',user_index,name="index"),   #首页
    path('login/',user_login,name="login"),    #登录
    path('register/',user_register,name='register'),  #注册
    path('problem/',user_problem,name='problem'),   #常见问题
    path("borrow/",user_borrow,name='borrow'),     #我要借款
    path("noticelist/",user_noticelist,name='noticelist'), #新手指引
    path('invest/',user_invest,name='invest')   #我要投资
]