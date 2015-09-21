from django.test import TestCase
from django.db import models
from jobs.models import Job
from django.utils import timezone
from model_mommy import mommy
from django.core import mail


class TestJob(TestCase):
    def setUp(self):
        self.job = mommy.prepare(Job)

    def tearDown(self):
        if len(Job.objects.all()) > 0:
            Job.objects.all().delete()

    def test_str_returns_company_and_position(self):
        entry = self.job
        self.assertEqual(str(entry), entry.company_name + " " + entry.position)

    def test_phone_not_required(self):
        self.job.phone = ""
        self.job.save()

        self.assertEquals(len(Job.objects.all()), 1)

    def test_external_link_not_required(self):
        job = mommy.make(Job, external_link = "")

        self.assertEquals(len(Job.objects.all()), 1)

    def test_token_is_added_pre_saving(self):
        self.job.save()
        self.assertNotEqual(self.job.token, '')

    def test_status_set_to_1_pre_saving(self):
        self.job.save()
        self.assertEqual(self.job.status, 1)

    def test_send_email_after_save(self):
        self.job.save()
        self.assertEquals(len(mail.outbox), 1)

    def test_do_not_send_email_after_update(self):
        self.job.save()
        self.job.save()

        self.assertEquals(len(mail.outbox), 1)

    def test_token_is_unique(self):
        firstjob = mommy.make(Job, token = '12345')
        secondjob = mommy.make(Job, token = '12345')

        self.assertNotEqual(firstjob.token, secondjob.token)

    def test_clean_description(self):
        self.job.description = "<p>&nbsp;test</p>"
        self.assertEqual(self.job.clean_description(), "&nbsp;test")

    def test_category_class_returns_slug(self):
        self.job.category = "Full Time"
        self.assertEqual(self.job.category_class(), "full-time")

    def test_category_class_returns_default(self):
        self.job.category = None
        self.assertEqual(self.job.category_class(), "default")

    def test_cities_returns_not_empty_list(self):
        self.assertNotEqual(len(self.job.cities), 0)

    def test_categories_returns_not_empty_list(self):
        self.assertNotEqual(len(self.job.categories), 0)
