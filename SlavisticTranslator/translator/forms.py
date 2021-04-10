from django import forms


class TextPostForm(forms.Form):
    content = forms.CharField(label='', widget=forms.Textarea)
