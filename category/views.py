from django.contrib.auth.models import User
from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from category.models import Category, Page, Comment

# Create your views here.
from myaccount.models import UserProfile


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
        context_dict['bkg'] = 'images/continent/' + category.slug + '.jpg'
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
        context_dict['bkg'] = "images/places/" + page.slug + ".jpg"
        if not request.user.username == "":
            user_profile = UserProfile.objects.get(user=request.user)
            user_rate = Comment.objects.filter(user=user_profile, wonder=page)
            if user_rate.count() > 0:
                context_dict['rate'] = user_rate[0].rate
            else:
                context_dict['rate'] = "no"
        else:
            context_dict['rate'] = "anonymouse"

        context_dict['comments'] = Comment.objects.filter(wonder=page)

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
        wonder = Page.objects.get(name=user_wonder)
        user_profile = UserProfile.objects.get(user=user)

        comment = Comment.objects.filter(user=user_profile, wonder=wonder)
        if comment.count() == 0:
            comment = Comment()
            comment.user = user_profile
            comment.rate = user_rate
            comment.comment = user_comment
            comment.wonder = wonder
            comment.save()
        else:
            comment = Comment.objects.filter(user=user_profile, wonder=wonder)[0]
            comment.rate = user_rate
            comment.comment = user_comment
            comment.save()

        # update page's rate
        ave_rate = Comment.objects.filter(wonder=wonder).aggregate(Avg('rate'))
        print(ave_rate)
        wonder.rate = ave_rate['rate__avg']
        wonder.save()

        return HttpResponse(-1)
