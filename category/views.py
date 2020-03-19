from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from category.models import Category, Page, Comment


# Create your views here.
def category(request, category_name_slug):
    context_dict = {}
    if category_name_slug == 'all':
        all_dict = {}
        all_dict['name'] = "ALL "
        pages = Page.objects.all()
        context_dict['pages'] = pages
        context_dict['category'] = all_dict
        context_dict['bkg'] = 'images/continent/all.jpg'
        return render(request, 'category/category.html', context=context_dict)
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
        context_dict['bkg'] = 'images/continent/'+category.slug+'.jpg'
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None

    return render(request, 'category/category.html', context=context_dict)

def category_select(request):
    return render(request, 'category/category_select.html')

def page(request, page_name_slug):
    context_dict = {}
    try:
        page = Page.objects.get(slug=page_name_slug)
        context_dict['page'] = page
        context_dict['bkg'] = "images/places/"+page.slug+".jpg"
    except Page.DoesNotExist:
        context_dict['page'] = None
    return render(request, 'category/page.html', context=context_dict)

@ensure_csrf_cookie
def submitComment(request):
    if request.method == "POST":
        print(request.POST)
        user_name = request.POST['userName']
        user_comment = request.POST['userComment']
        user_rate = request.POST['userRate']
        user_wonder = request.POST['userWonder']

        user = User.objects.get(username=user_name)
        wonder = Page.objects.get(slug=user_wonder)

        comment = Comment()
        comment.user = user
        comment.rate = user_rate
        comment.comment = user_comment
        comment.wonder = user_wonder
        comment.save()

        return HttpResponse(-1)