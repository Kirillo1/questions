from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

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


class ChoiceUpdateView(UpdateView):
    form_class = ChoiceForm
    template_name = "choice/choice_update_view.html"
    model = Choice
    success_url = reverse_lazy('poll:index')


class ChoiceDeleteView(DeleteView):
    template_name = "choice/choice_delete_view.html"
    model = Choice
    success_url = reverse_lazy('poll:index')
