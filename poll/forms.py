from django import forms

from poll.models import Poll


class PollForm(forms.ModelForm):
    question = forms.CharField(max_length=100, label='question')

    class Meta:
        model = Poll
        exclude = []
        widgets = {
            'poll': forms.CheckboxSelectMultiple
        }
