from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from category.models import Category, Page
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
        return HttpResponse(-1)
    else:
        print("get")
        return HttpResponse(-1)