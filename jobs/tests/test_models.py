from django.test import TestCase
from django.db import models
from jobs.models import Job
from django.utils import timezone


class TestJob(TestCase):
    def setUp(self):
        self.job = Job()
        self.job.company_name = "Company name"
        self.job.website = "http://pythonjobs.ie"
        self.job.position = "Developer"
        self.job.category = "Full time"
        self.job.location = "Dublin"
        self.job.description = "This is a good job. Go raibh míle maith agaibh!"
        self.job.email = "info@pythonjobs.ie"
        self.job.phone = "0123456789"
        self.job.external_link = "http://pythonjobs.ie"
        self.job.token = "lo11piq3i9q35yr8jou5"
        self.job.created_at = timezone.now()
        self.job.modified_at = timezone.now()
        self.job.status = 1
        self.job.save()

    def testDown(self):
        Job.objects.all().delete()

    def test_str_returns_company_and_position(self):
        entry = self.job
        self.assertEqual(str(entry), entry.company_name + " " + entry.position)

    def test_saved_utf8_characters(self):
        self.assertEqual(self.job.description,
                            "This is a good job. Go raibh míle maith agaibh!")

    def test_status_is_not_boolean(self):
        updated_job = self.job
        updated_job.status = "a"
        updated_job.save()
        self.job = Job.objects.first()
        self.assertEqual(self.job.status, 1)
        self.assertNotEqual(self.job.status, "a")
