from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from.models import Profile
from hotelmanagement.adminapp.models import Room_table


class SignUpform(UserCreationForm):
    first_name = forms.CharField(max_length=30, required='false', help_text='optional')
    first_name = forms.CharField(max_length=30, required='false', help_text='optional')
    email = forms.EmailField(max_length=254, help_text= 'Enter a valid email address')
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


class User_form(forms.ModelForm):
    class Meta:
        model= User
        fields = ('first_name', 'last_name', 'email',)


class staff_form(forms.ModelForm):
    profile_passport = forms.ImageField(required=False, label='profile_passport')
    means_of_identity = forms.ImageField(required=False, label='Means of identity')
    particulars = forms.FileField(required=False, label='particulars')
    class Meta:
        model = Profile
        fields = [
            'status',
            'address',
            'phone_number',
            'nationality',
            'state',
            'means_of_identity',
            'particulars',
            'profile_passport',
            'position',
            'marital_status',
            'staff',
        ]
    
class Room_form(forms.ModelForm):
    class Meta:
        model = Room_table
        fields = [
            'room_name',
            'price',
            'quantity',
            'description',
            'profile_picture',
            'category',
            'display_type',
        ]

        widgets = {
            'description':forms.Textarea(attrs={'cols':100, 'rows':10})
        }
