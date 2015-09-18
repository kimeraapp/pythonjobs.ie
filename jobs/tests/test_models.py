from django.test import TestCase
from django.db import models
from jobs.models import Job
from django.utils import timezone
from model_mommy import mommy


class TestJob(TestCase):
    def setUp(self):
        self.job = mommy.prepare(Job)

    def tearDown(self):
        Job.objects.all().delete()

    def test_str_returns_company_and_position(self):
        entry = self.job
        self.assertEqual(str(entry), entry.company_name + " " + entry.position)

    def test_phone_not_required(self):
        self.assertFalse(self.job_is_valid(self.job))

    def test_external_link_not_required(self):
        self.assertFalse(self.job_is_valid(self.job))

    def test_token_is_added_pre_saving(self):
        self.job.save()
        self.assertNotEqual(self.job.token, '')

    def test_status_set_to_1_pre_saving(self):
        self.job.save()
        self.assertEqual(self.job.status, 1)

    def test_token_is_unique(self):
        firstjob = mommy.make(Job, token = '12345')
        secondjob = mommy.make(Job, token = '12345')
        self.assertNotEqual(firstjob.token, secondjob.token)

    def test_get_clean_description(self):
        self.job.description = "<p>&nbsp;test</p>"
        self.assertEqual(self.job.get_clean_description(), "&nbsp;test")

    def job_is_valid(self, job):
        is_valid = True
        try :
            job.save()
        except :
            is_valid = False
