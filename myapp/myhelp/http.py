from django.http import JsonResponse


def render_json(code,msg):
    return JsonResponse({
        "code":code,
        "msg":msg,
    })