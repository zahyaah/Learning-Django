from django import forms
from django.core.exceptions import ValidationError

from .models import Remark


class RemarkForm(forms.ModelForm):
    class Meta:
        model = Remark
        fields = ("name", "text")
        labels = {
            'name': "Enter your name",
            'text': "Pen down your thoughts"
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb-5'})
        }

    def clean_text(self):
        text = self.cleaned_data["text"]
        if "Django" not in text:
            raise ValidationError("Only Google mails")
        return text
