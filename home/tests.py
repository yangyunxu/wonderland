from django.test import TestCase
from category.models import Page, Category
from django.urls import reverse
# Create your tests here.


class WhetherPagesCouldOpen(TestCase):
    def test(self):
        r1 = self.client.get(reverse('home:about'))
        r2 = self.client.get(reverse('home:faq'))
        r3 = self.client.get(reverse('home:contact'))
        self.assertEqual(r1.status_code, 200)
        self.assertEqual(r2.status_code, 200)
        self.assertEqual(r3.status_code, 200)


class IndexViewTests(TestCase):
    def test_index_view(self):
        category = Category.objects.get_or_create(name='China')[0]
        category.save()
        page1 = Page.objects.get_or_create(category=category, name='T', rate='10', intro='A long wall!')[0]
        page1.save()
        page2 = Page.objects.get_or_create(category=category, name='G', rate='10', intro='A long wall!')[0]
        page2.save()
        page3 = Page.objects.get_or_create(category=category, name='W', rate='7', intro='A long wall!')[0]
        page3.save()

        response = self.client.get(reverse('home:index'))
        self.assertEqual(response.status_code, 200)
        num_categories = len(response.context['pages'])
        self.assertEqual(num_categories, 2)
        self.assertContains(response, "T")
        self.assertContains(response, "G")





