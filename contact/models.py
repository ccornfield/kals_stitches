from django.db import models

class Contact(models.Model):
    email = models.EmailField(max_length=128, null=False, blank=False )
    subject = models.CharField(max_length=128, null=False, blank=False)
    body = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.subject
