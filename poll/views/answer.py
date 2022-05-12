from django.shortcuts import redirect
from django.views.generic import CreateView, ListView
from poll.forms import AnswerForm
from poll.models import Answer, Poll


class AnswerListView(ListView):
    model = Answer
    context_object_name = 'answers'
    template_name = "answer/answer_list_view.html"
    paginate_by = 5
    paginate_orphans = 0


class AnswerCreateView(CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = "answer/answer.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["poll"] = Poll.objects.get(pk=self.kwargs.get("pk"))
        return context

    def form_valid(self, form):
        answer = form.save(commit=False)
        answer.poll_id = self.kwargs.get("pk")
        answer.save()
        return redirect("poll:index")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["pk"] = self.kwargs.get("pk")
        return kwargs
