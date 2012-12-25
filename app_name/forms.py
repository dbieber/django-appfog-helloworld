from django import forms

class NewBetaUserForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name',
        widget=forms.TextInput(attrs={'placeholder': 'Jack Florey'}))
    email = forms.EmailField(label='Email',
        widget=forms.TextInput(attrs={'placeholder': 'you@example.com'}))

