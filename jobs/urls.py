from django.conf.urls import url
from jobs.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
]
