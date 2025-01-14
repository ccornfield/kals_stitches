from django.db import models
from profiles.models import UserProfile
from django.conf import settings
from django.contrib.auth.models import User

class Testimonies(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL,
                                    null=True, blank=True,)
    name = models.CharField(max_length=128, null=False, blank=False)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(null=False, blank=False)
    rating = models.CharField(max_length=1, null=True, blank=True)

    def __str__(self):
        return self.name
