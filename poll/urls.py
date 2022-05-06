from django.urls import path

from poll.views.polls import IndexView, PollDetailView, PollCreateView, PollUpdateView, PollDelete

app_name = "poll"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('poll/<int:pk>/', PollDetailView.as_view(), name="pool_detail_view"),
    path('poll/add/', PollCreateView.as_view(), name="poll_add"),
    path('poll/<int:pk>/update/', PollUpdateView.as_view(), name="poll_update"),
    path('poll/<int:pk>/delete/', PollDelete.as_view(), name="poll_delete"),
]