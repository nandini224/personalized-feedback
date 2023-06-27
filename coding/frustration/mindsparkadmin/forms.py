from django import forms

from mindsparkadmin.models import NotificationModel


class NotificationForm(forms.ModelForm):
    notifications = forms.CharField(widget=forms.Textarea(attrs={'cols': 22, 'rows': 3}))
    date= forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget)
    class Meta:
        model = NotificationModel
        fields = ('date','notifications',)
