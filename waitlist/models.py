from django.db import models


class Waitlist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    question = models.CharField(max_length=5000, null=True)
    response = models.CharField(max_length=5000)
    responded = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now=True)
