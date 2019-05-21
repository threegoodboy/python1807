from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from myapp.serializers import ProjectSerializer


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




class project_class(APIView):
    def get(self,request):
        queryset=''.objects.all()
        pg=PageNumberPagination()
        page_roles=pg.paginate_queryset(queryset,request,view=self)
        ser=ProjectSerializer(instance=page_roles,many=True)
        return Response(ser.data)
    def post(self,request):
        ser=ProjectSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)
