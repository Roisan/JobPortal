from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class JobSeeker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=15, null=True)

    def _str_(self):
        return self.user.username