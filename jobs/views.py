from django.views.generic import ListView
from jobs.models import Job


class IndexView(ListView):
    model = Job
    template_name = "index.html"
