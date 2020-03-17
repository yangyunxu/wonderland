from django.shortcuts import render
from myaccount.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
# Register to be a user
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
                  'myaccount/signup.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})

# Login for users
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                # record the date of login

                # Modify redirect page later
                return redirect(reverse('myaccount:signup'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'myaccount/login.html')


@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

# Logout for users
@login_required
def user_logout(request):
    logout(request)

    # Modify redirect page later
    return redirect(reverse('myaccount:signup'))