from django.urls import path

from poll.views.polls import IndexView, PollDetailView

app_name = "poll"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('poll/<int:pk>/', PollDetailView.as_view(), name="pool_detail_view"),
]