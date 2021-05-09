from django.contrib import admin
from .models import Publication, Author, Organization

# Register your models here.
admin.site.register(Publication)
admin.site.register(Author)
admin.site.register(Organization)