from django import forms

from .models import ContactSubmission


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ("name", "email", "message")
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your name",
                "maxlength": 120,
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "you@example.com",
                "maxlength": 254,
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "How can we help?",
                "maxlength": 5000,
            }),
        }
