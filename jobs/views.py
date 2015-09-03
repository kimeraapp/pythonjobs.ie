from django.views import generic
from jobs.models import Job


class IndexView(generic.ListView):
    model = Job
    template_name = "index.html"
    context_object_name = "jobs"


class ShowView(generic.DetailView):
    model = Job
    template_name = "show.html"


class NewView(generic.CreateView):
    model = Job
    fields = []
    template_name = "new.html"
