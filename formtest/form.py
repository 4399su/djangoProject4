from django import forms


class loginForm(forms.Form):
    sname = forms.CharField(max_length=30, label='姓名')
    spwd = forms.CharField(label='密码', widget=forms.PasswordInput)
