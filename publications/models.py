from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.


class BaseModel(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Organization(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Organizations"

    def __str__(self):
        return self.name


class Author(BaseModel):
    user = models.OneToOneField(
        User, blank=False, null=False, on_delete=models.CASCADE)

    organizations = models.ManyToManyField(Organization, blank=True)

    @property
    def name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        ordering = ['user']
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name


class Publication(BaseModel):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Author, blank=True, null=True, on_delete=models.SET_NULL)
    organization = models.ForeignKey(
        Organization, blank=True, null=True, on_delete=models.SET_NULL)
    publication_date = models.DateField(blank=False, null=False)
    document = models.FileField(upload_to='files/', blank=False, null=False,
                                validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    class Meta:
        ordering = ['publication_date']
        verbose_name_plural = "Publications"

    def __str__(self):
        return self.title
