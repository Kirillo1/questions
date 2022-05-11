from django import forms

from poll.models import Poll, Choice, Answer


class PollForm(forms.ModelForm):
    question = forms.CharField(max_length=100, label='question')

    class Meta:
        model = Poll
        exclude = []
        widgets = {
            'poll': forms.CheckboxSelectMultiple
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ("variant_text",)


class AnswerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        pk = kwargs.pop("pk")
        super().__init__(*args, **kwargs)
        self.fields['choice'].queryset = Choice.objects.filter(poll__pk=pk)

    class Meta:
        model = Answer
        exclude = ["poll"]
        widgets = {"choice": forms.widgets.RadioSelect(attrs={"class": "hello"})}
