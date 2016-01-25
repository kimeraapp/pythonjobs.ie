from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.db.models import signals
from django.utils.html import strip_tags
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.conf import settings
from pythonjobs.services import generate_token, send_confirmation_mail
from jobs.tasks import tweet


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

    cities = (
        'Antrim', 'Armagh', 'Carlow', 'Cavan', 'Clare', 'Cork', 'Derry',
        'Donegal', 'Down', 'Dublin', 'Fermanagh', 'Galway', 'Kerry',
        'Kildare', 'Kilkenny', 'Laois', 'Leitrim', 'Limerick', 'Longford',
        'Louth', 'Mayo', 'Meath', 'Monaghan', 'Offaly', 'Roscommon',
        'Sligo', 'Tipperary', 'Tyrone', 'Waterford', 'Westmeath',
        'Wexford', 'Wicklow', 'Other'
    )

    categories = (
        'Full time', 'Part time', 'Contract', 'Permanent',
        'Freelance', 'Internship', 'Other'
    )

    def __str__(self):
        return self.company_name + " " + self.position

    def clean_description(self):
        return strip_tags(self.description)

    def category_class(self):
        if self.category:
            return slugify(self.category)

        return "default"

    def get_absolute_url(self):
        return reverse('job-show', args=[str(self.id)])

    @staticmethod
    def get_actives(now=timezone.now()):
        limit = now - timedelta(days=120)
        return Job.objects.filter(
            status=1, created_at__gt=limit).order_by("-created_at").all()


def token_pre_save(signal, instance, sender, **kwargs):
    if not instance.token or Job.objects.filter(token=instance.token).exclude(id=instance.id):
        token = generate_token()
        while Job.objects.filter(token=token):
            token = generate_token()
        instance.token = token
        instance.status = 1


def mail_post_save(signal, instance, sender, created, **kwargs):
    if created and settings.DEBUG == False:
        send_confirmation_mail(instance)
        tweet.apply_async(args=(instance.get_absolute_url(),),
                          countdown=10, serializer='json')

signals.pre_save.connect(token_pre_save, sender=Job)
signals.post_save.connect(mail_post_save, sender=Job)
