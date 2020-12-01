from django.test import TestCase
from .models import Post
from wixaward.models import Profile
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import datetime


# Create your tests here.
class TestProject(TestCase):

    def tearDown(self) -> None:
        projects = Post.objects.all()
        if projects:
            for project in projects:
                project.delete()

    def setUp(self):
        projects = Post.objects.all()
        self.user = User(username='test_user')
        self.user.save()
        self.project = Post(

            
        )

    def test_project_instance(self):
        self.project.save()
        self.assertTrue(isinstance(self.project, Post))

    def test_save_project(self):
        self.project.save()
        query = Post.objects.all()
        self.assertIs(len(query), 0)

    def test_delete_project(self):

        self.project.save()
        self.project.delete()
        query = Post.objects.all()

        self.assertEqual(len(query),0)
