from django.db import models

class task(models.Model):
    title = models.CharField(max_length=200)
    descriptiion = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    create_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
