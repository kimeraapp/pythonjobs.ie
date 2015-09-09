from django.db import models
from django.db.models import signals
from pythonjobs.services import generate_token

class Job(models.Model):
    company_name = models.CharField(max_length=100)
    website = models.CharField(max_length=150)
    position = models.CharField(max_length=120)
    category = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    description = models.TextField()
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    external_link = models.CharField(max_length=200, blank=True)
    token = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    status = models.BooleanField(default=1)

    def __str__(self):
        return self.company_name + " " + self.position

    def __unicode__(self):
        return self.position

def token_pre_save(signal, instance, sender, **kwargs):
    token = generate_token()
    while Job.objects.filter(token = token):
        token = generate_token()
    instance.token = token;
    instance.status = 1

signals.pre_save.connect(token_pre_save, sender=Job)
