
from django.contrib.auth.models import User
from django.db import models


class Tarefa(models.Model):
    title = models.CharField(max_length=120)
    finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
