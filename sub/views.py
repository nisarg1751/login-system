# from email import message
# from os import uname
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from sub.forms import SignUp, EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.

#sing up form 
def sing_up(request):
    if request.method == 'POST':
        fm = SignUp(request.POST)
        if fm.is_valid():
            # fm.save()
            username=request.POST.get('username')
             # print("🚀 ~ file: views.py ~ line 17 ~ username", username)
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            password1=request.POST.get('password1')
            # print("🚀 ~ file: views.py ~ line 21 ~ password1", password1)
            email=request.POST.get('email')
            # print("🚀 ~ file: views.py ~ line 23 ~ email", email)
            myuser= User.objects.create_user(username=username,email=email,password=password1)
            myuser.save()
            messages.success(request,'your account created succesfully!!!!')
            fm = SignUp()
        else:
            fm = SignUp()
    else:
        fm = SignUp()
    return render(request,'signup.html',{'form':fm})

# login form

def login_hhh(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
        # if fm.is_valid():
        #     uname = fm.cleaned_data['username']
        #     upass = fm.cleaned_data['password']
            username = request.POST['username']
        # print("[][][][",username)
            password = request.POST['password']
            print(password)
        # print("ppppppp",password)

        # user = User.objects.get(username=username)
            user1 = authenticate(request, username = username, password = password)
            print(user1.password)
        
            print(user1)
            if user1 is not None:
                # print('!!!!!!!!!!!!!!!!dta is enter for authentication ')
                login(request, user1)
                # print('login sucessfully!!!!!!!!!!!!!!!!')
                return HttpResponseRedirect('/profile/')
            else:
                # print('something went wrong ')
                fm = AuthenticationForm()
        else:
            fm = AuthenticationForm()
        return render(request,'login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

  
#profile page
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = EditUserProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
            # uname = request.POST.get('username',)
            # name = request.POST.get('first_name',)
            # user.save()
                messages.success(request,'your data updated successfully!!!!')
            else:
                print("something went wrong-------------------------------------")
        else:
            fm = EditUserProfileForm(instance = request.user)        
        return render(request,'profile.html',{'name':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')

#logout page

def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def passwordchage(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            # SetPaaswordForm(user=request.user,data=request.POST)  for change password without old password
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'your password change succesfully!!!')
                return HttpResponseRedirect('/profile/')
            else:
                print('something went wrong!!!!!')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request,'password.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')


