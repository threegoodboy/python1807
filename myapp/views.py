from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from myapp.models import Users, Investment
from myapp.serializers import UserSerializer, InvestmentSerializer


def user_index(request):
    return render(request,"index.html")


def user_login(request):
    if request.method=='GET':
        return render(request,"login.html")
    elif request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')


def user_register(request):
    if request.method=='GET':
        return render(request,"register.html")
    elif request.method=='POST':
        pass


def user_invest(request):
    return render(request,"invest.html")

def user_problem(request):
    return render(request,"problem.html")

def user_borrow(request):
    return render(request,"borrow.html")

def user_noticelist(request):
    return render(request,"noticelist.html")








