from django import forms
from django.contrib.auth import (authenticate,get_user_model,)

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label="First Name",
                               widget=forms.TextInput({'class':'form-control',
                                                       'id':'fname',
                                                       'placeholder':'Email'}))

    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput({'class':'form-control',
                                                       'id':'pswd',
                                                       'placeholder':'Password'}))

    def clean(self, *args, **kwargs):

        username = self.cleaned_data.get("username").capitalize()

        password = self.cleaned_data.get("password")

        if username and password:

            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError("This user does not exist")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect passsword")

            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label="First Name",
                               widget=forms.TextInput({'class':'rcr-rcinputcontrol form-control-sm',
                                                       'id':'fname',
                                                       'placeholder':'First Name'}))
    lastname = forms.CharField(label="Last Name",
                               widget=forms.TextInput({'class': 'rcr-rcinputcontrol form-control-sm',
                                                       'id': 'lname',
                                                       'placeholder': 'Last Name'}))

    email = forms.EmailField(label='Email address',widget=forms.EmailInput({'class':'rcr-rcinputcontrol form-control-sm',
                                                       'id':'email',
                                                       'placeholder':'name@domain.com'}))
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput({'class':'rcr-rcinputcontrol form-control-sm',
                                                       'id':'pswd',
                                                       'placeholder':'Password'}))
    password2 = forms.CharField(label="Confirm password",
                                widget=forms.PasswordInput({'class': 'rcr-rcinputcontrol form-control-sm',
                                                        'id': 'pswd2',
                                                        'placeholder': 'Confirm Password'}))


    class Meta:

        model = User

        fields = [
            'username','lastname','email','password','password2',
        ]

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Password must match")
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return email

















