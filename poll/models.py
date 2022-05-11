from django.db import models

# Create your models here.
from django.urls import reverse


class BaseModel(models.Model):
    time_of_creations = models.DateTimeField(auto_now_add=True, verbose_name='time of creations')

    class Meta:
        abstract = True

    def get_absolute_url(self):
        return reverse("poll:pool_detail_view", kwargs={'pk': self.pk})


class Poll(BaseModel):
    question = models.CharField(max_length=100, verbose_name="question")

    def __str__(self):
        return f"{self.pk}: {self.question}"

    class Meta:
        db_table = 'poll'
        verbose_name = 'Poll'
        verbose_name_plural = 'Polls'


class Choice(BaseModel):
    variant_text = models.CharField(max_length=100, verbose_name="variant text")
    poll = models.ForeignKey("poll.Poll", on_delete=models.CASCADE, related_name="choices", verbose_name="Choice")

    class Meta:
        db_table = 'choice'
        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'

    def get_absolute_url(self):
        return reverse("poll:pool_detail_view", kwargs={'pk': self.pk})


class Answer(BaseModel):
    poll = models.ForeignKey("poll.Poll", on_delete=models.CASCADE, related_name='answers', verbose_name='poll')
    time_of_answer = models.DateTimeField(auto_now_add=True, verbose_name='time of answer')
    choice = models.ForeignKey("poll.Choice", on_delete=models.CASCADE, related_name='answers', verbose_name='choice')

    class Meta:
        db_table = 'answer'
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
