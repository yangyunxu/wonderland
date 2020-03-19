from django.contrib.auth.models import User
from myaccount.models import UserProfile
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('personalURL', 'picture',)

class ChangepwdForm(forms.Form):
    oldpassword = forms.CharField(
        required=True,
        label=u"original password",
        error_messages={'required': u'please enter original password'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"original password",
            }
        ),
    )
    newpassword1 = forms.CharField(
        required=True,
        label=u"new password",
        error_messages={'required': u'please enter new password'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"new password",
            }
        ),
    )
    newpassword2 = forms.CharField(
        required=True,
        label=u"check new password",
        error_messages={'required': u'please enter new password again'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"check new password",
            }
        ),
     )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"all blank should be filled")
        elif self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
            raise forms.ValidationError(u"Different passwords, check again!")
        else:
            cleaned_data = super(ChangepwdForm, self).clean()
        return cleaned_data


