from django import forms
from .models import RiderApplication, ContactMessage


class RiderApplicationForm(forms.ModelForm):
    class Meta:
        model = RiderApplication
        fields = ['full_name', 'phone', 'email', 'location', 'has_license', 'has_smartphone', 'has_motorbike', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Your full name', 'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'placeholder': '+254 700 000 000', 'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com', 'class': 'form-input'}),
            'location': forms.TextInput(attrs={'placeholder': 'e.g. Nairobi CBD, Westlands', 'class': 'form-input'}),
            'message': forms.Textarea(attrs={'placeholder': 'Tell us a bit about yourself...', 'rows': 4, 'class': 'form-input'}),
        }
        labels = {
            'has_license': 'I have a valid motorbike license',
            'has_smartphone': 'I have a smartphone with GPS',
            'has_motorbike': 'I have a reliable motorbike with delivery box',
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'phone', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name', 'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'placeholder': '+254 700 000 000', 'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com', 'class': 'form-input'}),
            'subject': forms.TextInput(attrs={'placeholder': 'How can we help?', 'class': 'form-input'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your message...', 'rows': 5, 'class': 'form-input'}),
        }
