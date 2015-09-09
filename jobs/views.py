from django.views import generic
from jobs.models import Job


class IndexView(generic.ListView):
    model = Job
    template_name = "index.html"
    context_object_name = "jobs"


class ShowView(generic.DetailView):
    model = Job
    template_name = "show.html"
    context_object_name = "job"


class NewView(generic.CreateView):
    model = Job
    fields = ['company_name', 'website', 'category', 'location', 'position',
              'description', 'email', 'phone', 'external_link', 'status']
    template_name = "new.html"
    success_url = "/"
