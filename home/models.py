from django.db import models

# Create your models here.

class User(models.Model):
  user_id = models.AutoField(primary_key=True)
  username = models.CharField(max_length=30)
  email = models.CharField(max_length=50,unique=True)
  password = models.CharField(max_length=50)
  
  # this is video ManaytoMany Relationship
  videos = models.ManyToManyField('Video', related_name='users', through='UserVideo')

  
  def __str__(self):
        return self.username

class Video(models.Model):
  video_id = models.AutoField(primary_key=True)
  video_file = models.FileField(upload_to='videos/%y', default='')
  title = models.CharField(max_length=30, default='')
  description = models.CharField(max_length=1000, default='')
  date = models.DateField( default='')
  status = models.CharField(max_length=10, default='')
  
  def __str__(self):
        return self.title
      
class UserVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    # Add other fields related to the relationship as needed, such as date_joined, watched_status, etc.

    def __str__(self):
        return f"User: {self.user.name}, Video: {self.video.title}"

