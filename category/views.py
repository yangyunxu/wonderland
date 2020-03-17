from django.shortcuts import render

# Create your views here.
def category(request, category_name_slug):
    context_dict = {}
    context_dict['category'] = category_name_slug

    return render(request, 'category/category.html', context=context_dict)

def category_select(request):
    return render(request, 'category/category_select.html')

def page(request, page_name_slug):
    context_dict = {}
    context_dict['page'] = page_name_slug
    return render(request, 'category/page.html', context=context_dict)