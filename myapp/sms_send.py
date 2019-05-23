
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import random

from myapp import cache


def create_code(phone):
    code=''.join([str(random.randint(0,9)) for _ in range(4)])

    cache.save_code(phone,code)

    #通过封装函数发送邀请码
    send_sms_code(phone,code)


def send_sms_code(phone, code):
    # coding=utf-8

    client = AcsClient('LTAIRiQGIywYBeYN', 'ZOHiNBYPr72dCFog2fLU5Pu9RvVAIf', 'cn-hangzhou')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', phone)
    request.add_query_param('SignName', "Disen工作室")
    request.add_query_param('TemplateCode', "SMS_128646125")
    request.add_query_param('TemplateParam', '{"code":"%s"}' % code)

    response = client. do_action_with_exception(request)
    # python2:  print(response)
    print(str(response, encoding='utf-8'))

if __name__ == '__main__':
    create_code(18501495624)