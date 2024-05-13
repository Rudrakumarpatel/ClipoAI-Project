from django.test import TestCase
from .models import User, Video

class ModelTestCase(TestCase):
    def test_create_user(self):
        # Test creating a User
        user = User.objects.create(username='testuser', email='test@example.com', password='testpassword')
        self.assertEqual(User.objects.count(), 1)  # Verify that the user was created

    def test_read_video(self):
        # Test reading a Video
        video = Video.objects.create(title='Test Video', description='This is a test video', date='2024-05-30', status='active')
        retrieved_video = Video.objects.get(title='Test Video')
        self.assertEqual(retrieved_video.description, 'This is a test video')  # Verify the video's description
        
#Run the test case using 
# python manage.py test
