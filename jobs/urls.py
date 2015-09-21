from django.conf.urls import url
from jobs.views import IndexView, ShowView, NewView, EditView

urlpatterns = [
    url(r'^jobs/new$', NewView.as_view(), name='job-new'),
    url(r'^jobs/(?P<pk>[0-9]+)/$', ShowView.as_view(), name='job-show'),
    url(r'^jobs/edit/(?P<slug>[A-Z0-9]+)$', EditView.as_view(slug_field="token"),
        name='job-edit'),
    url(r'^$', IndexView.as_view(), name='job-home'),
]
