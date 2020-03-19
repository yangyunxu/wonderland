from django.shortcuts import render
from category.models import Page
from category.models import Category
# Create your views here.
def theBestWonders(request):
    page_list = Page.objects.order_by('-rate')[:6]
    context_dict = {}
    context_dict['pages'] = page_list
    return render(request, 'search/thebestwonders.html', context=context_dict)

def searchResult(request, typestring):
    context_dict = {}
    categories = Category.objects.all()
    for category in categories:
        if typestring.lower() == category.name.lower():
            context_dict['results'] = Page.objects.filter(category=category).order_by('-rate')
            return render(request, 'search/searchpage.html', context=context_dict)
    pages = Page.objects.all()
    for page in pages:
        if typestring.lower() == page.name.lower():
            context_dict['results'] = Page.objects.get(name=typestring)
            return render(request, 'search/searchpage.html', context=context_dict)

    context_dict['results'] = None
    return render(request, 'search/searchpage.html', context=context_dict)

# def searchResult(request):
#     return render(request, 'search/searchpage.html')

