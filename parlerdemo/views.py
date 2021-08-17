from django.conf import settings
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import UpdateView
from parler.views import TranslatableUpdateView

from parlerdemo import forms
from parlerdemo import models


class HomeView(TemplateView):
    template_name = "parlerdemo/home.html"

    def get_context_data(self, **kwargs):
        di = super().get_context_data(**kwargs)
        di["blogs"] = models.Blog.objects.all()
        return di


class BlogUpdateView(TranslatableUpdateView):
    model = models.Blog
    form_class = forms.BlogForm
    success_url = "/"


class BlogDetailView(DetailView):
    model = models.Blog

    def get_context_data(self, **kwargs):
        di = super().get_context_data(**kwargs)
        di["LANGUAGES"] = settings.LANGUAGES
        return di
