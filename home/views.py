from django.shortcuts import render
from django.http import HttpResponse
from category.models import Page
from django.contrib.auth.models import User
from myaccount.models import UserProfile
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from search.views import searchResult

def index(request):
    page_list = Page.objects.order_by('-rate')[:2]
    context_dict = {}
    context_dict['pages'] = page_list
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'home/index.html', context=context_dict)


def about(request):
    # return HttpResponse("Wonderland says hey there is About page! <a href='/wonderland/'>Index</a>")
    return render(request, 'home/about.html')


def faq(request):
    return render(request, 'home/faq.html')


def contact(request):
    return render(request, 'home/contact.html')



