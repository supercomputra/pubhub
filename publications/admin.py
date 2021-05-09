from django.contrib import admin
from .models import *

# Register your models here.


class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "author",
                    "publication_date")


admin.site.register(Publication, PublicationAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "modification_date", "creation_date")


admin.site.register(Author, AuthorAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "modification_date", "creation_date")


admin.site.register(Organization, OrganizationAdmin)
