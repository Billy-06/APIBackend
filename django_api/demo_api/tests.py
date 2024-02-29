# Test cases for the demo_api app
from django.test import TestCase

# Testing the views
from django.urls import reverse
from rest_framework import status

# Testin the models
from demo_api.models import Project, User, Article

class ProjectTestCase(TestCase):
    """
    Test case for the Project model
    """
    def setUp(self):
        """
        Create a project object
        """
        self.project = Project.objects.create(
            name="Test Project",
            about="This is a test project",
            concepts="Python|Django",
            github="https://github.com",
            image="https://image.com"
        )

    def test_project_creation(self):
        """
        Test the project object creation
        """
        self.assertTrue(isinstance(self.project, Project))
        self.assertEqual(self.project.__str__(), self.project.name)

class UserTestCase(TestCase):
    """
    Test case for the User model
    """
    def setUp(self):
        """
        Create a user object
        """
        self.user = User.objects.create(
            name="Test User",
            email="me@you.mail",
            password="test"
        )

    def test_user_creation(self):
        """
        Test the user object creation
        """
        self.assertTrue(isinstance(self.user, User))
        self.assertEqual(self.user.__str__(), self.user.name)

class ArticleTestCase(TestCase):
    """
    Test case for the Article model
    """
    def setUp(self):
        """
        Create an article object
        """
        self.article = Article.objects.create(
            title="Test Article",
            content="This is a test article",
            author="Test User",
            image="https://image.com"
        )

    def test_article_creation(self):
        """
        Test the article object creation
        """
        self.assertTrue(isinstance(self.article, Article))
        self.assertEqual(self.article.__str__(), self.article.title)

# 
# TESTING THE  VIEWS
# 

class ProjectViewTestCase(TestCase):
    """
    Test case for the Project views
    """
    def setUp(self):
        """
        Create a project object
        """
        self.project = Project.objects.create(
            name="Test Project",
            about="This is a test project",
            concepts="Python|Django",
            github="https://github.com",
            image="https://image.com"
        )

    def test_project_list(self):
        """
        Test the project list view
        """
        response = self.client.get(reverse('project_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.project.name)

    def test_project_details(self):
        """
        Test the project details view
        """
        response = self.client.get(reverse('project_details', args=[self.project.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.project.name)

    def test_project_update(self):
        """
        Test the project update view
        """
        response = self.client.put(reverse('project_details', args=[self.project.pk]), {
            "name": "Test Project Updated",
            "about": "This is a test project updated",
            "concepts": "Python|Django|React",
            "github": "https://github.com",
            "image": "https://image.com/updated"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Test Project Updated")

    def test_project_delete(self):
        """
        Test the project delete view
        """
        response = self.client.delete(reverse('project_details', args=[self.project.pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class UserViewTestCase(TestCase):
    """
    Test case for the User views
    """
    def setUp(self):
        """
        Create a user object
        """
        self.user = User.objects.create(
            name="Test User",
            email="me@you.mail",
            password="test"
        )

    def test_user_list(self):
        """
        Test the user list view
        """
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.user.name)

    def test_user_details(self):
        """
        Test the user details view
        """
        response = self.client.get(reverse('user_details', args=[self.user.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.user.name)

    def test_user_update(self):
        """
        Test the user update view
        """
        response = self.client.put(reverse('user_details', args=[self.user.pk]), {
            "name": "Test User Updated",
            "email": "me@her.mial",
            "password": "test"
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Test User Updated")

    def test_user_delete(self):
        """
        Testing the user delete view
        """
        response = self.client.delete(reverse('user_details', args=[self.user.pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ArticleViewTestCase(TestCase):
    """
    Test case for the Article views
    """
    def setUp(self):
        """
        Create an article object
        """
        self.article = Article.objects.create(
            title="Test Article",
            content="This is a test article",
            author="Test User",
            image="https://image.com"
        )

    def test_article_list(self):
        """
        Test the article list view
        """
        response = self.client.get(reverse('article_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.article.title)

    def test_article_details(self):
        """
        Test the article details view
        """
        response = self.client.get(reverse('article_details', args=[self.article.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.article.title)

    def test_article_update(self):
        """
        Test the article update view
        """
        response = self.client.put(reverse('article_details', args=[self.article.pk]), {
            "title": "Test Article Updated",
            "content": "This is a test article updated",
            "author": "Test User",
            "image": "https://image.com/updated"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Test Article Updated")

    def test_article_delete(self):
        """
        Test the article delete view
        """
        response = self.client.delete(reverse('article_details', args=[self.article.pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
