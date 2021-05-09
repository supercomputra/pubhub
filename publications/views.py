import os

from django.http import FileResponse
from django.shortcuts import render, get_object_or_404
from wsgiref.util import FileWrapper

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from .models import Publication, Author
from django.db.models import Q
from django import forms
from django.urls import reverse  # new


class HomeView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Publication
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Publication.objects.filter(
            Q(title__icontains=query) |
            Q(author__user__first_name__icontains=query) |
            Q(author__user__last_name__icontains=query) |
            Q(organization__name__icontains=query)
        )


class AuthorView(TemplateView):
    template_name = 'author.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["publications"] = Publication.objects.filter(
            author__user=self.request.user)
        return self.render_to_response(context)


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'publication_date', 'author',
                  'document']
        widgets = {
            'author': forms.HiddenInput(),
            'publication_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }


class CreatePublicationForm(CreateView):  # new
    model = Publication
    form_class = PublicationForm
    template_name = 'publication_form.html'

    def get_success_url(self):
        return reverse('publication', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        publication = form.save(commit=True)
        author = Author.objects.get(user=self.request.user)
        if author is None:
            author = Author.objects.create(user=user)

        publication.author = author
        publication.save()
        return super().form_valid(form)


class PublicationDetailView(DetailView):
    model = Publication
    template_name = 'publication_detail.html'
