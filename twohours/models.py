import random
from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import bizzfuzz


class User(AbstractUser):
    birthday = models.DateTimeField('Birthday date')
    random = models.IntegerField('Random', default=lambda: random.randint(0, 100))

    def as_bizzfuzz(self):
        return bizzfuzz(self.random)