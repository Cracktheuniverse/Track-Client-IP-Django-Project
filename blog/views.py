from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm , UserCreationForm,LoginForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post

# Create your views here.
def home(request):
    posts=Post.objects.all()
    ip=request.session.get('ip',0)
    return render(request,'blog/home.html',{'posts':posts})

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')


def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        ip=request.session.get('ip',0)
        return render(request,'blog/dashboard.html',{'posts':posts},{'ip':ip})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


# def user_signup(request):
#     if request.method=="POST":
#      form =SignUpForm(request.POST)
#      if form.is_valid():
#         form.save()
#      else:
#         form= SignUpForm() 
#     return render(request,'blog/signup.html',{'form':form})

def user_signup(request):
 if request.method=="POST":
  form=SignUpForm(request.POST)
  if form.is_valid():
      messages.success(request,"congratulations registration successful!! ")
      form.save()
 else:
            form=SignUpForm()
 return render(request,'blog/signup.html',{'form':form})








def user_login(request):
 if not request.user.is_authenticated:
    if request.method=="POST":
        form=LoginForm(request=request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return HttpResponseRedirect('/dashboard/')
    else:
        form=LoginForm()
        return render(request,'blog/login.html',{'form':form})
 else:
    return HttpResponseRedirect('/dashboard')



def add_post(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=PostForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc=form.cleaned_data['desc']
                pst=Post(title=title,desc=desc)
                pst.save()
                form=PostForm()
        else:
            form=PostForm()
            return render (request,'blog/addpost.html')
                
      
    else:
        return HttpResponseRedirect('/login/')

def update_post (request,id):
    if request.user.is_authenticated:
        return render (request,'blog/updatepost.html')
    else:
        return HttpResponseRedirect('/login/')
    
def delete_post(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')


        
    