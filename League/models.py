from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Player(models.Model):
    """
    Represents a single player in the league
    """
    
    user = models.OneToOneField(User)
    