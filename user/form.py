from django import forms


class UserProfileForm(forms.Form):
    first_name = forms.CharField(label='first name', max_length=20)
    last_name = forms.CharField(label='last name', max_length=20)
    email = forms.EmailField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    date = forms.DateField(label='birth date')
    password = forms.CharField(label='password', max_length=10, widget=forms.PasswordInput)
    # FB = forms.URLField(label='FB', max_length=60)
    picture = forms.ImageField(label='Profile Picture')
    country = forms.CharField(label='Country', max_length=20)
    phone = forms.CharField(label='phone number', max_length=11)
