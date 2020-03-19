import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','wonderland.settings')
import django
django.setup()
from myaccount.models import UserProfile
from django.contrib.auth.models import User

def populate():
    user1 ={'username': 'fengqiu',
            'password': '123456',
            'email': '123456@163.com'}
    user2 = {'username': 'yunxuyang',
             'password': '123456',
             'email': '123456@163.com'}
    user3 = {'username': 'yuli',
             'password': '123456',
             'email': '123456@163.com'}
    user4 = {'username': 'xiaotongwang',
             'password': '123456',
             'email': '123456@163.com'}

    userprofile1 = {'user': user1,
                    'logInDate': '2019-03-03',
                    'personalURL': '',
                    'picture': ''}
    userprofile2 = {'user': user2,
                    'logInDate': '2019-03-03',
                    'personalURL': '',
                    'picture': ''}
    userprofile3 = {'user': user3,
                    'logInDate': '2019-03-03',
                    'personalURL': '',
                    'picture': ''}
    userprofile4 = {'user': user4,
                    'logInDate': '2019-03-03',
                    'personalURL': '',
                    'picture': ''}
    add_userprofile(userprofile1['user'], userprofile1['logInDate'], userprofile1['personalURL'], userprofile1['picture'])
    add_userprofile(userprofile2['user'], userprofile2['logInDate'], userprofile2['personalURL'], userprofile2['picture'])
    add_userprofile(userprofile3['user'], userprofile3['logInDate'], userprofile3['personalURL'], userprofile3['picture'])
    add_userprofile(userprofile4['user'], userprofile4['logInDate'], userprofile4['personalURL'], userprofile4['picture'])

def add_userprofile(user, logInDate, personalURL, picture):
    u = User.objects.create_user(username=user['username'], password=user['password'], email=user['email'])
    up = UserProfile.objects.get_or_create(user=u)[0]
    up.logInDate = logInDate
    up.personalURL = personalURL
    up.picture = picture
    up.save()
    return up
if __name__ == '__main__':
    print('Starting myaccount population script...')
    populate()
