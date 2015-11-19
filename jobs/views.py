from django.views import generic
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from jobs.models import Job


class IndexView(generic.ListView):
    model = Job
    template_name = "index.html"
    context_object_name = "jobs"
    queryset = Job.get_actives()


class ShowView(generic.DetailView):
    model = Job
    template_name = "show.html"
    context_object_name = "job"

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        return get_object_or_404(Job, pk=pk, status=1)


class NewView(generic.CreateView):
    model = Job

    fields = ['company_name', 'website', 'category', 'location', 'position',
              'description', 'email', 'phone', 'external_link', 'status']

    template_name = "new.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(generic.CreateView, self).get_context_data(**kwargs)

        context['cities'] = Job.cities
        context['categories'] = Job.categories

        return context


class EditView(generic.UpdateView):
    model = Job

    fields = ['company_name', 'website', 'category', 'location', 'position',
              'description', 'email', 'phone', 'external_link', 'status']

    template_name = "edit.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(generic.UpdateView, self).get_context_data(**kwargs)

        context['cities'] = Job.cities
        context['categories'] = Job.categories

        return context


class JobsFeed(Feed):
    title = "Python Jobs Ireland"
    link = "/rss"
    description = "Latest jobs on Python Jobs Ireland: pythonjobs.ie"

    def items(self):
        return Job.objects.order_by('-created_at')[:10]

    def item_title(self, job):
        return job.position

    def item_description(self, job):
        return job.description

    def item_author_name(self, job):
        return 'pythonjobs.ie'

    def item_pubdate(self, job):
        return job.created_at

    def item_link(self, job):
        return reverse('job-show', args=[job.pk])
