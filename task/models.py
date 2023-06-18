from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True, verbose_name='Profile Picture')
    bio = models.TextField(blank=True, null=True)
    following = models.ManyToManyField(
        "self",
        related_name="follower",
        symmetrical=False,
        blank=True
    )

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {} {}".format(self.user, self.title, self.created)
    
    class Meta:
        ordering = ['complete']