from django import forms

class EnterHTML(forms.Form):
    enterHTML = forms.CharField(required = False, widget=forms.Textarea(attrs={"rows":10, "cols":80}))
    enterHTML_Convert = forms.CharField(required = False, widget=forms.Textarea(attrs={"rows":10, "cols":80}))