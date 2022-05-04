from django.views.generic import ListView

from poll.models import Poll


class IndexView(ListView):
    model = Poll
    context_object_name = 'polls'
    template_name = "polls/index.html"
    paginate_by = 5
    paginate_orphans = 0

    def get_queryset(self):
        return Poll.objects.order_by('-time_of_creations')
