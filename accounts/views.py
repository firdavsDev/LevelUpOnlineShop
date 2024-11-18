from django.contrib import messages  # for send messages to frontend
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login

from .models import CustomUser


def login(request):
    if request.method == "POST":
        print("######################################################################################")
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        print(user_email)
        print(user_password)

        #here we filter user model
        have =  CustomUser.objects.filter(email=user_email).exists()
        #here check
        if  have != True:
            messages.error(request, 'Invalid Email')
            return redirect("login")
        
        user = authenticate(username=user_email, email=user_email, password=user_password)
        print("user",user)
        
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect("login")
        else:
            auth_login(request, user)
            return redirect('home_page')
        
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        f_name = request.POST.get("f_name")
        l_name = request.POST.get("l_name")
        user_email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        # check if email already exists
        user = CustomUser.objects.filter(email=user_email)
        if user:
            messages.error(request, "Email is already taken")
            return redirect("register")

        user_obj = CustomUser.objects.create(
            username=user_email,
            first_name=f_name,
            last_name=l_name,
            email=user_email,
            password=password1,
        )
        print(user_obj.email)
        # print("User created")
        messages.success(request, "Account created successfully")
        return redirect("login")

    return render(request, "accounts/register.html")
