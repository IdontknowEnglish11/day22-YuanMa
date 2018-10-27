from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        user=request.POST.get('user')
        pwd=request.POST.get('pwd')
        if user=='root' and pwd=='123':
            request.session['username']=user
            request.session['is_login']=True
            return redirect('/index/')
        else:
            return render(request,'login.html')

def index(request):
    if request.session.get('is_login',None):
        return render(request,'index.html')
    else:
        return HttpResponse('gun')


def logout(request):
    request.session.clear()
    return redirect('/login/')


from django.views.decorators.cache import cache_page

# @cache_page(5)
def test1(request):
    import time
    v=time.time()
    return render(request,'test.html',{'v':v})





################ Form ################
from django.forms import Form
from django.forms import widgets
from django.forms import fields
class FM(Form):
    user=fields.CharField(error_messages={'required':'用户名不能为空.'})
    pwd=fields.CharField(widget=widgets.PasswordInput(attrs={'class':'c1'}),
        max_length=12,
        min_length=6,
        error_messages={'required':'密码不能为空.','max_length':'密码长度不能大于12','min_length':'密码长度不能小于6'})
    email=fields.EmailField(error_messages={'required':'邮箱不能为空.','invalid':'邮箱格式错误'})


def fm(request):
    if request.method=='GET':
        obj=FM()
        return render(request,'fm.html',{'obj':obj})
    elif request.method=='POST':
        obj=FM(request.POST)
        ri=obj.is_valid()
        if ri:
            print(obj.cleaned_data)
        else:
            print(obj.errors)
            return render(request,'fm.html',{'obj':obj})











# def test(request):
#     print('没带钱')
#     return HttpResponse('OK')













