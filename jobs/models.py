from django.db import models


class Job(models.Model):
    company_name = models.CharField(max_length=100)
    website = models.CharField(max_length=150)
    position = models.CharField(max_length=120)
    category = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    description = models.TextField()
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    external_link = models.CharField(max_length=200)
    token = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    status = models.BooleanField(default=1)

    def __str__(self):
        return self.company_name + " " + self.position
