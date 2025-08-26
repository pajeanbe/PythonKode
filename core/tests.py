from django.test import TestCase
from django.urls import reverse
from .models import Topic, Article, User

class CoreModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.topic = Topic.objects.create(title='Test Topic', slug='test-topic')
        self.article = Article.objects.create(
            topic=self.topic,
            title='Test Article',
            slug='test-article',
            content='This is a test article.',
            author=self.user
        )

    def test_topic_creation(self):
        self.assertEqual(self.topic.title, 'Test Topic')
        self.assertEqual(self.topic.slug, 'test-topic')

    def test_article_creation(self):
        self.assertEqual(self.article.title, 'Test Article')
        self.assertEqual(self.article.slug, 'test-article')
        self.assertEqual(self.article.topic, self.topic)
        self.assertEqual(self.article.author, self.user)


class CoreViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.topic = Topic.objects.create(title='Test Topic', slug='test-topic')
        self.article = Article.objects.create(
            topic=self.topic,
            title='Test Article',
            slug='test-article',
            content='This is a test article.',
            author=self.user
        )

    def test_topic_list_view(self):
        response = self.client.get(reverse('core:topic_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.topic.title)

    def test_topic_detail_view(self):
        response = self.client.get(reverse('core:topic_detail', args=[self.topic.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.topic.title)
        self.assertContains(response, self.article.title)

    def test_article_detail_view(self):
        response = self.client.get(reverse('core:article_detail', args=[self.topic.slug, self.article.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.article.title)
        self.assertContains(response, self.article.content)
