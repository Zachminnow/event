from django import forms
from django.core.exceptions import ValidationError
from .models import SellModel, Vendor


class SellForm(forms.ModelForm):
    class Meta:
        model = SellModel
        fields = ['product', 'vendor', 'unit', 'description']
        widgets = {
            'product': forms.TextInput(attrs={'class': 'form-control'}),
            'vendor': forms.TextInput(attrs={'class': 'form-control'}),
            'unit': forms.NumberInput(attrs={'class': 'form-control', 'initial': '0'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        def clean_vendor(self):
            vendor_name = self.cleaned_data.get('vendor.name')
            
            if not Vendor.objects.filter(name=vendor_name).exists():
                raise ValidationError("This vendor does not exist.")
            return vendor_name 

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'email', 'first_name', 'last_name',
                  'phone_number', 'business_address',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 
                                           'placeholder': 'Business/Company Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'e.g., vendor@example.com'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Contact First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Contact Last Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': '+254712345678'}),
            'business_address': forms.Textarea(attrs={'class': 'form-control',
                                                      'rows': 3,
                                                      'placeholder': 'Full business address'}),
        }
