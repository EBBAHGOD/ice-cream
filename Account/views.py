from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):

    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['Password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Sorry invalid credentials")
            return redirect('login')













    else:
        return render(request,'login.html')




def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        second_name=request.POST['second_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        user_name=first_name+ " "+second_name
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                print("sorry username taken")
                messages.info(request,'username taken')
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                print("sorry email already used")
                messages.info(request,'Email already used')
                return render(request,'register.html')
            else:
                user_input=User.objects.create_user(first_name=first_name,last_name=second_name,email=email,password=password1,username=user_name)
                user_input.save()
                print("user created")
                return redirect('login')
        else:
            print("sorry paswords do not match")
            return render(request,'register.html')

        
     
 



    else:
        return render(request,'register.html')