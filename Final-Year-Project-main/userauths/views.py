from django.shortcuts import redirect, render
from django.conf import settings
from userauths.forms import UserRegisterForm
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

User = settings.AUTH_USER_MODEL

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username} your account created successfully..")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1']
            )
            # login(request, new_user)
            return redirect("userauths:login")
        
    else:
        print("User cant Registered")
        form = UserRegisterForm()

    context = {
        'form':form
    }
    return render(request, "register.html", context)


def login(request):
    context = {}

    if request.user.is_authenticated:
        return redirect("Shwet_Multimetal_Company:home")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect("Shwet_Multimetal_Company:home")
        else:
            messages.warning(request, "Invalid email or password.")

    return render(request, "login.html", context)
        

def logout_view(request):
    print("Logout view called")  # Add this line for debugging
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("userauths:login")

# from django.shortcuts import redirect, render
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from userauths.forms import UserRegisterForm  # Assuming you have a UserRegisterForm in userauths/forms.py
# from django.conf import settings

# User = settings.AUTH_USER_MODEL  # Use the configured User model

# def register_view(request):
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             username = form.cleaned_data.get("username")
#             messages.success(request, f"Hey {username}, your account has been created successfully!")
#             new_user = authenticate(username=new_user.email, password=form.cleaned_data['password1'])
#             login(request)
#             return redirect("Shwet_Multimetal_Company:login")  # Assuming you have a login URL pattern
#         else:
#             messages.error(request, "Registration failed. Please fix the errors below.")  # Use messages.error for errors
#     else:
#         form = UserRegisterForm()

#     context = {'form': form}
#     return render(request, "register.html", context)



