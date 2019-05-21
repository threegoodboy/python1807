from django.urls import path

from myapp.views import *

app_name='myapp'
urlpatterns = [
    path('hello/',hello),
    path('login/',user_login,name="login"),
    path('register/',user_register,name='register'),
    path('problem/',user_problem,name='problem'),
]