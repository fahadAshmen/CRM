from django import forms
from . models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=155, widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password',
    'class':'form-control'}))
    confirm__Password = forms.CharField(max_length=155, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
    'class':'form-control'}))
    class Meta:
        model = User
        fields = ['email','username','phone','password',]

    def __init__(self, *args,**kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Enter E-mail'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username' 
        self.fields['phone'].widget.attrs['placeholder'] = 'Enter Phone-number' 
        # self.fields['password'].widget.attrs['placeholder'] = 'Enter Password'
    
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    def clean(self):
        cleaned_data= super().clean()
        password = cleaned_data.get('password')
        confirm__Password = cleaned_data.get('confirm__Password')
        print('Pass & Con Pass=', password, confirm__Password)
        if password != confirm__Password:
            raise ValidationError('Password and Confirm Password not same')
        return cleaned_data
    

