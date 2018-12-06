from django import forms



class NameForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=30)