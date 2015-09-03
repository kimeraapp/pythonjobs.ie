from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from jobs.models import Job


class TestJob(TestCase):
    def setUp(self):
        self.client = Client()
        self.job = Job()
        self.job.title = "test"
        self.job.company = "company test"
        self.job.url = "pythonjobs.ie"
        self.description = "Testing"
        self.job.save()

    def testDown(self):
        Job.objects.all().delete()

    def test_index_returns_200(self):
        response = self.client.get(reverse("job-home"))
        self.assertEquals(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "index.html")

    def test_show_returns_200(self):
        response = self.client.get(reverse("job-show", args=[self.job.pk]))
        self.assertEquals(response.status_code, 200)

    def test_show_template(self):
        response = self.client.get(reverse("job-show", args=[self.job.pk]))
        self.assertTemplateUsed(response, "show.html")

    def test_new_returns_200(self):
        response = self.client.get(reverse("job-new"))
        self.assertEquals(response.status_code, 200)

    def test_new_template(self):
        response = self.client.get(reverse("job-new"))
        self.assertTemplateUsed(response, "new.html")
