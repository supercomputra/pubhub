from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class Publication(BaseModel):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ['modification_date']

    def __str__(self):
        return self.title


class Organization(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Author(BaseModel):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, blank=False, null=False, on_delete=models.CASCADE)
    publications = models.ManyToManyField(Publication, blank=True)
    organizations = models.ManyToManyField(Organization, blank=True)

    @property
    def name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.name