#django
from django.db import models
from django.contrib.auth.models import User

from users.models import ProfileUser
# Create your models here.
# Also You can import a model like '{file.py}.{class or method}
class Post(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    profileUser = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    title=models.CharField(max_length=250)
    photo= models.ImageField(
        upload_to='posts/photos'
    )
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by @{self.user.username}'

