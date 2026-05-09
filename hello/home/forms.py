from django import forms

from .models import ContactSubmission

MESSAGE_MAX_LENGTH = 5000


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
                "maxlength": MESSAGE_MAX_LENGTH,
            }),
        }

    def clean_message(self):
        # The model field is TextField (no DB-level cap); maxlength on the
        # widget is HTML-only and is bypassed by curl / scripted POSTs.
        # Enforce the cap server-side.
        msg = self.cleaned_data["message"]
        if len(msg) > MESSAGE_MAX_LENGTH:
            raise forms.ValidationError(
                f"Message must be {MESSAGE_MAX_LENGTH} characters or fewer."
            )
        return msg
