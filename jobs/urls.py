from django.conf.urls import url
from jobs.views import IndexView, ShowView

urlpatterns = [
    url(r'^/jobs/(?P<pk>[0-9]+)/$', ShowView.as_view(), name='job-show'),
    url(r'^$', IndexView.as_view(), name='job-home'),
]
