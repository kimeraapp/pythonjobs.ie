from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict
from jobs.models import Job


class TestJob(TestCase):
    def setUp(self):
        self.client = Client()
        self.job = Job()
        self.job.position = "test"
        self.job.company_name = "company test"
        self.job.website = "pythonjobs.ie"
        self.job.category = "full"
        self.job.description = "Testing"
        self.job.email = "test@test.com"
        self.job.location = "Testing"
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

    def test_create_new_job(self):
        self.job.pk = 0
        params = model_to_dict(self.job)
        response = self.client.post(reverse("job-new"), params)
        self.assertEquals(response.status_code, 302)
