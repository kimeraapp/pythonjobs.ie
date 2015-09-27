from django.test import TestCase
from unittest.mock import patch
from pythonjobs.services import Twitter
from jobs.tasks import tweet


class TestTweet(TestCase):
    def setUp(self):
        self.patcher = patch.object(Twitter, 'tweet')
        self.mock_tweet = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_tweet_calls_twitter_class(self):
        tweet(1)
        self.assertTrue(self.mock_tweet.called)
