from django import forms
from django.core.exceptions import ValidationError
from .models import Remark


class RemarkForm(forms.ModelForm):
    class Meta:
        model = Remark
        fields = ("name", "text")

    def clean_text(self):
        text = self.cleaned_data["text"]
        if "@gmail" not in text:
            raise ValidationError("Only Google mails")
        return text
