from django.shortcuts import render,redirect
from django.http import HttpResponse
# import psycopg2
from .models import *
# def trail(request):
#     return render(request,"empview.html")
def homeview(request):
    return render(request,"home.html")
def hr_login(request):
    return render(request,"hrlogin.html")
def emp_login(request):
    return render(request,"emplogin.html")

def hrview(request):
    x=HRMAN.objects.all()
    u=int(request.POST['id'])
    p=request.POST['password']
    flag=0
    for i in x:
        if(i.hrid==u and i.psd==p):
            flag=1
    if(flag==1):
        return render(request,"hrview.html")
    else:
        return HttpResponse("Invalid Login")

def home(request):
    if 'user' in request.session:
        current_user=request.session['user']
        param={'current_user':current_user}
        return render(request,'empview.html',param)
    else:
        return redirect('empln')
    return render(request,'emplogin.html')

def empview(request):
    if request.method=="POST":
        name=request.POST.get('id')
        password=request.POST.get('password')
        check_user=EMP.objects.filter(empid=name,psd=password)
        if check_user:
            request.session['user']=name
            return redirect("home")
        else:
            return HttpResponse("Invalid")
    return render(request,'emplogin.html')
def logoutx(request):
    try:
        del request.session['user']
    except:
        return redirect('empvw')
    return redirect('empvw')

def add_employe(request):
    return render(request,"addemp.html")
def emp_remove(request):
    return render(request,"removeemp.html")
def change_password(request):
    return render(request,"changepsd.html")
def register(request):
    a=request.POST['n1']
    b=request.POST['n2']
    c=request.POST['n3']
    d=request.POST['n4']
    e=request.POST['n5']
    data=EMP(name=a,dept=b,empid=c,mob=d,psd=e)
    data.save()
    return HttpResponse("successfully registered")
def password_change(request):
    a=request.POST['b1']
    b=request.POST['b2']
    c=request.POST['b3']
    HRMAN.objects.filter(psd=a).update(psd=b)
    return HttpResponse("password change")

def delete_employee(request):
    a=request.POST['c1']
    b=request.POST['c2']
    data=EMP.objects.filter(empid=b)
    data.delete()
    return HttpResponse('Employee deleted successfully')

def leave_form(request):

    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        return render(request,"leavereq.html",param)
    else:
        return redirect("empln")
def empl_psd(request):
    if 'user' in request.session:
        return render(request, "chngepsd.html")
    else:
        return redirect("home")
def ps_change(request):
    a=request.POST['b1']
    b=request.POST['b2']
    c=request.POST['b3']
    EMP.objects.filter(psd=a).update(psd=b)

    return HttpResponse("password change")
def leaveregister(request):

    param = request.POST['userid']
    ltype=request.POST['type']
    ldays=request.POST['Number']
    lmsg=request.POST['message']
    ldata=leavreq(ltype=ltype,ldays=ldays,lmsg=lmsg,lid=param)
    s = EMP.objects.filter(empid=param).update(status='3')
    ldata.save()
    return HttpResponse("Added data")


# def leaveregisterz(request):
#     s=EMP.objects.get(id=id)
#     if request.method == 'POST':
#         form = C
#

# Create your views here.

def edata(request):
    data = EMP.objects.all()
    return render(request, "empdata.html", {'data': data})
    return render(request,"empdata.html")

def leaveview(request):
    data=leavreq.objects.all()

    return render(request,"leaveapplication.html",{'data':data,})

def Approve(request,lidx):

    # lid=request.POST['lidx']
    EMP.objects.filter(empid=lidx).update(status='2')
    return HttpResponse("Approved")
def Deny(request,lidx):
    EMP.objects.filter(empid=lidx).update(status='1')
    return HttpResponse("Denied Leave")