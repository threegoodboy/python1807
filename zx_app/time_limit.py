import datetime

from zx_app.models import Investment


def tm_li(id):
    old_time = Investment.objects.get(id=id).make_time
    old_time = datetime.datetime.strptime(old_time,"%Y-%m-%d %H:%M:%S")
    time_li = Investment.objects.get(id=id).time_limit
    now_time = datetime.datetime.now()
    if (now_time - old_time).days <= time_li:
        return True
    else:
        return False
