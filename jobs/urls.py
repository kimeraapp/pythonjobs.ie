from django.conf.urls import url
from jobs.views import IndexView, ShowView, NewView

urlpatterns = [
    url(r'^/jobs/(?P<pk>[0-9]+)/$', ShowView.as_view(), name='job-show'),
    url(r'^/jobs/new/$', NewView.as_view(), name='job-new'),
    url(r'^$', IndexView.as_view(), name='job-home'),
]
