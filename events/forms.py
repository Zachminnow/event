from django import forms
from .models import EventModel, EventBook


class EventForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = ['title', 'host', 'guest', 'description', 'venue', 'date', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'title': forms.TextInput(attrs={'class': 'form'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'host': forms.TextInput(attrs={'class': 'form-control'}),
            'guest': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class EventBookForm(forms.ModelForm):
    class Meta:
        model = EventBook
        fields = ['first_name', 'last_name', 'gender', 'ticket_category']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'ticket_category': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['gender'].label = "Gender"
        self.fields['ticket_category'].label = "Ticket Category"

        # Add help text for ticket categories
        self.fields['ticket_category'].help_text = "Select your preferred ticket category"
