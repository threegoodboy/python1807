from django.urls import path


from myapp.views import *

app_name='myapp'

urlpatterns = [
    path('index/',user_index,name="index"),
    path('login/',user_login,name="login"),
    path('register/',user_register,name='register'),
    path('problem/',user_problem,name='problem'),
    path("borrow/",user_borrow,name='borrow'),
    path("noticelist/",user_noticelist,name='noticelist'),
    path('invest/',user_invest,name='invest'),
]