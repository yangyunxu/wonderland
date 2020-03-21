from django.shortcuts import render
from myaccount.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from myaccount.models import UserProfile
from django.utils import timezone
from category.models import Comment, Page



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
                profile = UserProfile.objects.get(user=user)
                lastLogin = profile.logInDate
                currentLogin = timezone.now()
                profile.logInDate = currentLogin
                profile.save()
                qs1 = Comment.objects.filter(user=profile).order_by('date')[:3]
                qs2 = Comment.objects.filter(user=profile).order_by('rate')[:5]
                pages = {}
                for item in qs2:
                    wonder_name = item.wonder
                    page = Page.objects.get(name=wonder_name)
                    pages[wonder_name] = page
                return render(request, 'myaccount/myaccount.html', context={'profile': profile, 'lastLogin': lastLogin, 'qs1': qs1, 'pages':pages})
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
    return redirect(reverse('myaccount:login'))

@login_required
def myaccount(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    lastLogin = profile.logInDate
    currentLogin = timezone.now()
    profile.logInDate = currentLogin
    profile.save()
    qs1 = Comment.objects.filter(user=profile).order_by('-date')[:3]
    qs2 = Comment.objects.filter(user=profile).order_by('-rate')[:5]
    pages = {}
    for item in qs2:
        wonder_name = item.wonder
        page = Page.objects.get(name=wonder_name)
        pages[wonder_name] = page
    return render(request, 'myaccount/myaccount.html', context={'profile': profile, 'lastLogin': lastLogin, 'qs1': qs1, 'pages':pages})


def changepwd(request):
    if request.method == 'POST':
        user = request.user
        oldpassword = request.POST.get('oldpassword')
        newpassword = request.POST.get('newpassword')
        newpassword1 = request.POST.get('newpassword1')
        if newpassword != oldpassword:
            if newpassword == newpassword1:
                user.set_password(newpassword)
                user.save()
                return render(request, 'myaccount/login.html')
            else:
                return HttpResponse("Different passwords, check again!")
        else:
                return HttpResponse("New password must differ from the old!")
    else:
        return render(request, 'myaccount/changepwd.html')








