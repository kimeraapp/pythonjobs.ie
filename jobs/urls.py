from django.conf.urls import url
from django.conf.urls.static import static
from jobs.views import IndexView, ShowView, NewView
from pythonjobs import settings

urlpatterns = [
    url(r'^jobs/new$', NewView.as_view(), name='job-new'),
    url(r'^jobs/(?P<pk>[0-9]+)/$', ShowView.as_view(), name='job-show'),
    url(r'^$', IndexView.as_view(), name='job-home'),
] + static(settings.STATIC_URL)
