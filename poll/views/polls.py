from django.db.models import Count, ExpressionWrapper as E, F, DecimalField
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from poll.forms import PollForm
from poll.models import Poll


class IndexView(ListView):
    model = Poll
    context_object_name = 'polls'
    template_name = "polls/index.html"
    paginate_by = 5
    paginate_orphans = 0

    def get_queryset(self):
        return Poll.objects.order_by('-time_of_creations')


class PollDetailView(DetailView):
    template_name = 'polls/poll_detail_view.html'
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        count = self.object.answers.count()
        context["count"] = count
        context["choices"] = self.get_choices_with_answers_count(count, self.object.choices.all())
        return context

    def get_choices_with_answers_count(self, count, choices):
        f = 100 / count
        percent = E(F("answer_count") * f, output_field=DecimalField())
        res_choices = choices.annotate(answer_count=Count("answers__pk")).annotate(percent=percent)
        return res_choices


class PollCreateView(CreateView):
    model = Poll
    form_class = PollForm
    template_name = "polls/poll_create.html"


class PollUpdateView(UpdateView):
    form_class = PollForm
    template_name = "polls/poll_update.html"
    model = Poll

    def get_success_url(self):
        return reverse("poll:pool_detail_view", kwargs={"pk": self.object.pk})


class PollDelete(DeleteView):
    template_name = "polls/poll_delete.html"
    model = Poll
    success_url = reverse_lazy('poll:index')
