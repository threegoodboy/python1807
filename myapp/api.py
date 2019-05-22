

from myapp.myhelp.http import render_json


def get_code(request):
    if request.method=="GET":

        return render_json()
    return render_json(100,"不允许GET外的请求")
