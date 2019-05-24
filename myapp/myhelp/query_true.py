from django.shortcuts import render




def decide(request,msg):
    if msg is None:
        mydict={}
        mydict['%serror'%(msg)]='%s不能为空'%(msg)
        return mydict
    else:
        mydict=None
        return mydict