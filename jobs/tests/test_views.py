from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict
from model_mommy import mommy
from jobs.models import Job
from jobs.views import JobsFeed


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
        self.job.report_clicks = 4
        self.job.save()

    def testDown(self):
        Job.objects.all().delete()

    def test_index_returns_200(self):
        response = self.client.get(reverse("job-home"))
        self.assertEquals(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "index.html")

    def test_index_list_active_jobs(self):
        mommy.make(Job, status=0)
        response = self.client.get(reverse("job-home"))
        self.assertEquals(len(response.context["jobs"]), 1)

    def test_show_returns_200(self):
        response = self.client.get(reverse("job-show", args=[self.job.pk]))
        self.assertEquals(response.status_code, 200)

    def test_show_template(self):
        response = self.client.get(reverse("job-show", args=[self.job.pk]))
        self.assertTemplateUsed(response, "show.html")

    def test_show_inactive_job_returns_404(self):
        job = mommy.make(Job, status=0)
        response = self.client.get(reverse("job-show", args=[job.pk]))
        self.assertEquals(response.status_code, 404)

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

    def test_edit_returns_200(self):
        response = self.client.get(reverse("job-edit", args=[self.job.token]))
        self.assertEquals(response.status_code, 200)

    def test_edit_template(self):
        response = self.client.get(reverse("job-edit", args=[self.job.token]))
        self.assertTemplateUsed(response, "edit.html")
		
    def test_report_returns_200(self):
        response = self.client.get(reverse("report_click", args=[self.job.pk]))
        self.assertEquals(response.status_code, 302)
	
    def test_feed_items_returns_not_empty_list(self):
        self.assertNotEqual(len(JobsFeed.items(self)), 0)

    def test_feed_title_returns_job_position(self):
        item = self.job
        self.assertEquals(JobsFeed.item_title(self, item), item.position)

    def test_feed_description_returns_job_description(self):
        feed_description = JobsFeed.item_description(self, self.job)
        self.assertEquals(feed_description, self.job.description)

    def test_feed_author_name_returns_job_pythonjobs_ie(self):
        feed_author = JobsFeed.item_author_name(self, self.job)
        self.assertEquals(feed_author, 'pythonjobs.ie')

    def test_feed_pubdate_returns_job_created_at(self):
        feed_pubdate = JobsFeed.item_pubdate(self, self.job)
        self.assertEquals(feed_pubdate, self.job.created_at)

    def test_feed_link_returns_job_link(self):
        job_link = reverse('job-show', args=[self.job.pk])
        self.assertEquals(JobsFeed.item_link(self, self.job), job_link)
