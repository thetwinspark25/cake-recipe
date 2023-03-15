from django.shortcuts import render,redirect
from .models import Recipedb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from recipe_userapp.models import Contact

# Create your views here.

def adminindex(request):
    return render(request,'adminindex.html')
def addrecipe(request):
    if request.method=="POST":
        rcpname=request.POST.get('rname')
        img_l=request.FILES['rimg']
        rcpinstr=request.POST.get('rinstr')
        rcpingr=request.POST.get('ringr')
        data=Recipedb(recipe_name=rcpname,recipe_image=img_l,instruction=rcpinstr,ingredients=rcpingr)
        data.save()
    return render(request,'addrecipe.html')
    
def sample(request):
    return render(request,'sample.html')

def demo(request):
    return render(request,'demo.html')

def view_recipe(request):
    data=Recipedb.objects.all()
    return render(request,'view_recipe.html',{'data':data})

def edit(request,id):
    data=Recipedb.objects.filter(id=id)
    return render(request,'edit.html',{'data':data})

def update(request,id):
    if request.method=="POST":
        rcpname=request.POST.get('rname')
        try:
            img_l=request.FILES['rimg']
            fs=FileSystemStorage()
            file=fs.save(img_l.name,img_l)
        except MultiValueDictKeyError:
            file=Recipedb.objects.get(id=id).recipe_image
        rcpinstr=request.POST.get('rinstr')
        rcpingr=request.POST.get('ringr')
        Recipedb.objects.filter(id=id).update(recipe_name=rcpname,recipe_image=file,instruction=rcpinstr,ingredients=rcpingr)

    return redirect('view_recipe')
def delete(request,id):
    Recipedb.objects.filter(id=id).delete()
    return redirect('view_recipe')

def adlogin(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username_a'] = username
            request.session['password_a'] = password
            return redirect('adminindex')
        else:
            return render(request,'adlogin.html', {'msg':'Sorry Invalid User Credentials'})
    else:
        return render(request, 'adlogin.html')

def contact(request):
    data=Contact.objects.all()
    return render(request,'view_contact.html',{'data':data})

def adlogout(request):
    del request.session['username_a']
    del request.session['password_a']
    return redirect('adlogin')
