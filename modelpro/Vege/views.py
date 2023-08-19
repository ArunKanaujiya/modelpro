from django.shortcuts import render,redirect,get_object_or_404
from Vege.models import Receipe
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def receipes(request):
    if request.method=='POST':
        data=request.POST 
        receipe_image=request.FILES.get('receipe_image')
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image,
              )
        
        return redirect('/receipe/')
    
    queryset=Receipe.objects.all()
    if request.GET.get('search'):
        queryset=Receipe.objects.filter(receipe_name__icontains=request.GET.get('search'))
    
    return render(request,'myapp/receipe.html')

@login_required(login_url='/login/')
def ShowReceipe(request):
    queryset=Receipe.objects.all()
    context={'queryset':queryset}
    return render(request,'myapp/index.html',context)

@login_required(login_url='/login/')
def delete_receipe(request,id):
    queryset=get_object_or_404(Receipe,id=id)
    queryset.delete()
    return redirect('/index/')

@login_required(login_url='/login/')
def update_receipe(request,id):
   queryset=get_object_or_404(Receipe,id=id)
   if request.method=='POST':
        data=request.POST
        receipe_image=request.FILES.get('receipe_image')
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description
        if receipe_image:
            queryset.receipe_image=receipe_image
        queryset.save()
        
        return redirect('/index')
   
   return render(request,'myapp/update.html')

def login_page(request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request,'invalid username')
            return redirect('/login/')
        
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'invalid password')
            return redirect('/login')
        else:
            login(request,user)
            return redirect('/index')
        
        return render(request,'myapp/login.html')

def register_page(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'user already taken...')
            return redirect('/register')
        
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        messages.info(request,'Account created succesfully..')
        return redirect('/login')
    return render(request,'myapp/register.html')

def logout_page(request):
    logout(request)
    print("This Is logout Page..")
    return render(request,'myapp/logout.html')