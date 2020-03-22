from django.test import TestCase
from category.models import Page, Category
from django.urls import reverse
# Create your tests here.
class TheBestWondersViewTests(TestCase):
    def test_thebestwonders_view(self):
        category = Category.objects.get_or_create(name='China')[0]
        category.save()
        page1 = Page.objects.get_or_create(category=category, name='T', rate='10', intro='A long wall!')[0]
        page1.save()
        page2 = Page.objects.get_or_create(category=category, name='H', rate='10', intro='A long wall!')[0]
        page2.save()
        page3 = Page.objects.get_or_create(category=category, name='E', rate='10', intro='A long wall!')[0]
        page3.save()
        page4 = Page.objects.get_or_create(category=category, name='G', rate='10', intro='A long wall!')[0]
        page4.save()
        page5 = Page.objects.get_or_create(category=category, name='R', rate='10', intro='A long wall!')[0]
        page5.save()
        page6 = Page.objects.get_or_create(category=category, name='A', rate='10', intro='A long wall!')[0]
        page6.save()
        page7 = Page.objects.get_or_create(category=category, name='W', rate='7', intro='A long wall!')[0]
        page7.save()

        response = self.client.get(reverse('search:thebestwonders'))
        self.assertEqual(response.status_code, 200)
        num_categories = len(response.context['pages'])
        self.assertEqual(num_categories, 6)
        self.assertContains(response, "T")
        self.assertContains(response, "H")
        self.assertContains(response, "E")
        self.assertContains(response, "G")
        self.assertContains(response, "R")
        self.assertContains(response, "A")

