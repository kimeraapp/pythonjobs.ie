from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=300)
    company = models.CharField(max_length=50)
    description = models.TextField()

