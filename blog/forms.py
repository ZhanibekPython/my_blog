from datetime import date

from django import forms

from .models import *


class NewEventForm(forms.Form):
    name = forms.CharField(label='Title', max_length=30)
    description = forms.CharField(label='Description', max_length=30)
    date_publ = forms.DateField(label='Date', initial=date.today())
    author = forms.ModelChoiceField(label='Author', queryset=Author.objects.all())
    content = forms.CharField(label='Content', widget=forms.Textarea(attrs={'cols': 80, 'rows': 6}))
    image = forms.ImageField()


class NewAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'