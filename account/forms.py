from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username or Email'
        
        self.fields['password'].label = ''
        self.fields['password'].widget.attrs['placeholder'] = 'Enter Password'
    
    login_save = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(),
        label='Remember me ?'
    )
    
class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='', 
        widget=forms.TextInput(attrs={
            'class':'form-control', 
            'placeholder':'Enter your Email Address'
            }
        )
    )
    # password1 = forms.Field(
    #     label="Password", 
    #     widget=forms.PasswordInput(attrs={
    #         'class':'form-control', 
    #         'placeholder':'',
    #         'help_text':'<li>Your password must contain at least 8 characters.</li>',
    #         }
    #     )
    # )
    # password2 = forms.Field(
    #     label="Password", 
    #     widget=forms.PasswordInput(attrs={
    #         'class':'form-control', 
    #         'placeholder':'',
    #         'help_text':'<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>',
    #         }
    #     )
    # )
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email
    
    def __init__(self, *args, **kwargs):
        super(CustomRegisterForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your Username'
        self.fields['username'].help_text = ''

        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password1'].help_text = (
            '<ul class="form-text text-muted small">'
            '<li>Your password must contain at least 8 characters.</li>'
            '<li>Your password cannot be entirely numeric.</li>'
            '</ul>'
        )
        
        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].help_text = (
            '<span class="form-text">'
            '<p>Enter the same password as before</p>'
            '</span>'	
        )
    # use later
    
    #     first_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your first name.')
    #     last_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your last name.')
    
    # def __init__(self, *args, **kwargs):
    #     super(Form, self).__init__(*args, **kwargs)
        
    #     self.fields['password2'].widget.attrs['class'] = 'form-control'
    #     self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
    #     self.fields['password2'].label = ''
    #     self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	
