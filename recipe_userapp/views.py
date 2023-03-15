from django.shortcuts import render,redirect
from recipe_adminapp.models import Recipedb
from .models import Contact,Register
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def userindex(request):
    return render(request,'userindex.html')

def view_rec(request):
    data=Recipedb.objects.all()
    return render(request,'view_rec.html',{'data':data})

def recipe_detail(request,id):
    data=Recipedb.objects.filter(id=id)
    return render(request,'recipe_detail.html',{'data':data})

def contact(request):
    if request.method == "POST":
        nm=request.POST.get('name')
        em=request.POST.get('email')
        sb=request.POST.get('subject')
        msg=request.POST.get('message')
        data=Contact(name=nm,email=em,subject=sb,message=msg)
        data.save()
    return render(request,'contact.html')

def register(request):
    if request.method == "POST":
       uname=request.POST.get('name') 
       passw=request.POST.get('pass')
       email=request.POST.get('email')
       ph=request.POST.get('phone')
       data=Register(username=uname,password=passw,email=email,phone=ph)
       data.save()
    return render(request,'register.html')

def login(request):
    if request.method == "POST":
        username_l = request.POST.get('uname')
        password_l= request.POST.get('pass')
        if Register.objects.filter(username=username_l,password=password_l).exists():
            data =  Register.objects.filter(username=username_l,password=password_l).values('email','phone','id').first()
            #request.session['uname'] = data['name']
            request.session['uemail'] = data['email']
            request.session['umobile'] = data['phone']
            request.session['username'] = username_l
            request.session['password'] = password_l
            request.session['uid'] = data['id']
            return redirect('userindex')
        else:
            return render(request,'login.html', {'msg':'Sorry Invalid User Credentials'})
    return render(request,'login.html')

def logout(request):
    del request.session['uemail']
    del request.session['umobile']
    del request.session['username']
    del request.session['password']
    del request.session['uid'] 
    return redirect('userindex')