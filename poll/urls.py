from django.urls import path

from poll.views.answer import AnswerCreateView, AnswerListView
from poll.views.choice import ChoiceCreateView, ChoiceUpdateView, ChoiceDeleteView
from poll.views.polls import IndexView, PollDetailView, PollCreateView, PollUpdateView, PollDelete

app_name = "poll"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('poll/<int:pk>/', PollDetailView.as_view(), name="pool_detail_view"),
    path('poll/add/', PollCreateView.as_view(), name="poll_add"),
    path('poll/<int:pk>/update/', PollUpdateView.as_view(), name="poll_update"),
    path('poll/<int:pk>/delete/', PollDelete.as_view(), name="poll_delete"),
    path('choice/<int:pk>/add/', ChoiceCreateView.as_view(), name="choice_add"),
    path('choice/<int:pk>/update/', ChoiceUpdateView.as_view(), name="choice_update"),
    path('choice/<int:pk>/delete/', ChoiceDeleteView.as_view(), name="choice_delete"),
    path('answer/<int:pk>/create/', AnswerCreateView.as_view(), name="answer"),
    path('answers/', AnswerListView.as_view(), name="answer_list_view"),
]