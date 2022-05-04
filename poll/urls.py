from django.urls import path

from poll.views.polls import IndexView

app_name = "poll"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
]