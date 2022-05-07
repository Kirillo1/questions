from django.shortcuts import redirect
from django.views.generic import DetailView, CreateView

from poll.forms import ChoiceForm
from poll.models import Choice, Poll


class ChoiceView(DetailView):
    model = Choice
    template_name = "polls/poll_detail_view.html"


class ChoiceCreateView(CreateView):
    model = Choice
    template_name = 'choice/choice_create_view.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        choice = form.save(commit=False)
        choice.poll = Poll.objects.get(pk=self.kwargs.get("pk"))
        choice.save()
        return redirect("poll:pool_detail_view", pk=choice.poll.pk)
