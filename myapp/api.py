

from myapp.myhelp.http import render_json
from myapp import sms_send


def get_onecode(request):         #手机验证码
    if request.method == 'GET':
        # 获取查询参数 phonenum
        print(1111111111)
        phonenum = request.GET.get('phonenum', None)



        if phonenum is None:
            return render_json(201, '请求参数phone是必填项')

        sms_send.create_code(phonenum)
        return render_json(200, '获取验证码成功!')

    return render_json(100,  '只允许GET请求')
