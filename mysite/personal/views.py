from django.shortcuts import render

from django.contrib.auth.models import User
from django.shortcuts import render, redirect


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect



# Create your views here.

def home_screen_view(request):
	print(request.headers)
	return render(request, "personal/home.html",{})

def login_view(request):
	print(request.headers)
	return render(request,"personal/login.html",{})



# register view is used to create a new user

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        # If the user already exists
        if User.objects.filter(username=username).exists():
            user_exists = True
            return render(request, 'personal/login.html', {'user_exists': user_exists})
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            return redirect('home')
    return render(request, 'register.html')



# login view is for signing into an existing user.

def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('logbook')   

        else:
            # Return an error message  the login credentials are incorrect.
            error_message = 'Invalid username or password.'
            return render(request, 'personal/home.html', {'error_message': error_message})
    else:
        return redirect(request, 'login')
