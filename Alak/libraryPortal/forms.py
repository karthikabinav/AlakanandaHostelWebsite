from django import forms
from Alak.libraryPortal import models
from models import * 

class BorrowForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.filter(isVisible=True))
    
    class Meta:
        model = BookOrder
        fields = ('books')
    
    