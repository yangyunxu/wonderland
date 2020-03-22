from django.test import TestCase
from category.models import Category, Page, Comment
from django.urls import reverse
from myaccount.models import UserProfile
from django.contrib.auth.models import User
# Create your tests here.
def add_category(name):
    category = Category.objects.get_or_create(name=name)[0]
    category.save()
    return category

class CategorySelectViewTests(TestCase):
    def test_catgory_select_view(self):
        response = self.client.get(reverse('category:categories'))
        self.assertEqual(response.status_code, 200)

class CategoryViewTests(TestCase):
    def test_category_view_with_category(self):
        category = add_category('North America')
        response = self.client.get(reverse('category:category', args=[category.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "North America")
class PageViewTests(TestCase):
    def test_page_view_with_page(self):
        category = Category.objects.get_or_create(name='China')[0]
        category.save()
        page = Page.objects.get_or_create(category=category, name='The Great Wall', rate='8', intro='A long wall!')[0]
        page.save()
        response = self.client.get(reverse('category:page', args=[page.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The Great Wall")




