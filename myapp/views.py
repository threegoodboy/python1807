from django.shortcuts import render


def user_index(request):
    return render(request,"index.html")


def user_login(request):
    return render(request,"login.html")

def user_register(request):
    return render(request,"register.html")

def user_invest(request):
    return render(request,"invest.html")

def user_problem(request):
    return render(request,"problem.html")

def user_borrow(request):
    return render(request,"borrow.html")

def user_noticelist(request):
    return render(request,"noticelist.html")