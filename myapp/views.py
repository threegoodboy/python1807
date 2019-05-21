from django.shortcuts import render


def hello(request):
    return render(request,"index.html")


def user_login(request):
    return render(request,"login.html")

def user_register(request):
    return render(request,"register.html")

def user_problem(request):
    return render(request,"problem.html")