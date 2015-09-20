from django.views import generic
from jobs.models import Job


class IndexView(generic.ListView):
    model = Job
    template_name = "index.html"
    context_object_name = "jobs"
    queryset = Job.objects.order_by("-created_at").all()


class ShowView(generic.DetailView):
    model = Job
    template_name = "show.html"
    context_object_name = "job"


class NewView(generic.CreateView):
    model = Job

    fields = ['company_name', 'website', 'category', 'location', 'position',
              'description', 'email', 'phone', 'external_link', 'status']
    cities = Job.cities
    categories = Job.categories

    template_name = "new.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(generic.CreateView, self).get_context_data(**kwargs)

        context['cities'] = self.cities
        context['categories'] = self.categories

        return context

class EditView(generic.UpdateView):
    model = Job

    fields = ['company_name', 'website', 'category', 'location', 'position',
              'description', 'email', 'phone', 'external_link', 'status']
    cities = Job.cities
    categories = Job.categories

    template_name = "edit.html"
    success_url = "/" 

    def get_context_data(self, **kwargs):
        context = super(generic.UpdateView, self).get_context_data(**kwargs)

        context['cities'] = self.cities
        context['categories'] = self.categories

        return context
