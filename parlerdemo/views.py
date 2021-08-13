from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from parler.views import TranslatableUpdateView

from parlerdemo import forms
from parlerdemo import models


class MyModelUpdateView(TranslatableUpdateView):
    model = models.MyModel
    form_class = forms.MyModelForm
    success_url = "/admin/"


class MyModelDetailView(DetailView):
    model = models.MyModel

