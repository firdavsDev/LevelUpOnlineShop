from django.contrib import messages  # for send messages to frontend
from django.db import transaction
from django.shortcuts import redirect, render

from cart.models import Cart
from cart.utils import get_session_key

from ..models import CustomUser
from ..forms import RegistarForm



# def login(request):
#     if request.method == "POST":
#         user_email = request.POST.get("email")
#         password = request.POST.get("password")

#         user = authenticate(email=user_email, password=password)
#         if user is not None:
#             auth_login(request, user)
#             messages.success(request, "Logged in successfully")
#             return redirect("home")
#         else:
#             messages.error(request, "Login or password is incorrect")
#             return redirect("login")
#     return render(request, "accounts/login.html")

# here we filter user model


########################## it's mine
# def login(request):
#     if request.method == "POST":
#         print("######################################################################################")
#         user_email = request.POST.get('email')
#         user_password = request.POST.get('password')
#         print(user_email)
#         print(user_password)
#         have =  CustomUser.objects.filter(email=user_email).exists()
#         #here check
#         if  have != True:
#             messages.error(request, 'Invalid Email')
#             return redirect("login")

#         user = authenticate(username=user_email, email=user_email, password=user_password)
#         print("user",user)

#         if user is None:
#             messages.error(request, "Invalid Password")
#             return redirect("login")
#         else:
#             auth_login(request, user)
#             return redirect('home_page')

#     return render(request, 'accounts/login.html')


@transaction.atomic
def register(request):
    try:
        registar_form = RegistarForm()
        if request.method == "POST":
            registar_form = RegistarForm(data=request.POST)
            if registar_form.is_valid():
                user_obj = registar_form.save()

                session_key = get_session_key(request)
                cart_obj, _ = Cart.objects.get_or_create(session_key=session_key)
                cart_obj.user = user_obj
                cart_obj.save()
                messages.success(request, "Account created successfully")
                context = {
                    "registar_form":registar_form,
                }
                return redirect("login")
        context = {
            "registar_form":registar_form,
        }
        return render(request, "accounts/register.html", context)
    except Exception as e:
        messages.error(request, f"Error creating account: {e}")
        return redirect("register")


