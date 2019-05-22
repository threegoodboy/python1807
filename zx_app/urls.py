from django.urls import path

from zx_app.views import *

app_name = 'ZXJR'

urlpatterns = [
    path('main/',main_index,name='main'),
    path('reg/',register,name='reg'),
    path('log/',login,name='login')
]
