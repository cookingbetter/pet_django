from django import forms
from .models import Receipt


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ('name', 'type', 'cooking_time', 'img', 'instruction')
    
    favorite = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))