from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# Create your models here.

class UrlShort(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=CASCADE)
    original = models.URLField(null=True) #200
    short = models.CharField(max_length=50, unique=True, null=True)
    visits = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.original + "--"

class IpData(models.Model):
    url = models.ForeignKey(UrlShort, null=True, on_delete=CASCADE)
    ip_addr = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)