from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from jobs.views import IndexView, ShowView, NewView, EditView, JobsFeed #, ReportView
from .models import Job
from . import views

info_job = {
    'queryset': Job.get_actives(),
    'data_field': 'modified_at',
}

urlpatterns = [
    url(r'^jobs/new$', NewView.as_view(), name='job-new'),
    url(r'^jobs/(?P<pk>[0-9]+)/$', ShowView.as_view(), name='job-show'),
    url(r'^jobs/edit/(?P<slug>[A-Z0-9]+)$',
        EditView.as_view(slug_field="token"), name='job-edit'),
    url(r'^$', IndexView.as_view(), name='job-home'),
    url(r'^rss/$', JobsFeed()),
    url(r'^robots\.txt$',
        TemplateView.as_view(template_name='robots.txt', content_type='text/plain'),
        name="robots"),
    url(r'^sitemap\.xml$',
        sitemap,
        {'sitemaps': {'jobs': GenericSitemap(info_job, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),
	#url(r'^jobs/(?P<pk>[0-9]+)/report$', ReportView.as_view, name='report_click'),
	url(r'^jobs/(?P<pk>[0-9]+)/report$', views.report, name='report_click'),
]
