from django import forms
from django.utils.translation import get_language
from parler.forms import TranslatableModelForm

from parlerdemo import models


class BlogForm(TranslatableModelForm):
    class Meta:
        model = models.Blog
        fields = "__all__"

    @property
    def language(self):
        return get_language()
