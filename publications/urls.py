from django.urls import path

from .views import *

urlpatterns = [
    path('search', SearchResultsView.as_view(), name='search_results'),
    path('', HomeView.as_view(), name='home'),
    path('author', AuthorView.as_view(), name='author'),
    path('publication/<pk>', PublicationDetailView.as_view(), name='publication'),
    path('publication', CreatePublicationForm.as_view(), name='publication_form'),
]
