from django import forms
from django.utils.translation import get_language
from parler.forms import TranslatableModelForm

from parlerdemo import models


class MyModelForm(TranslatableModelForm):

    class Meta:
        model = models.MyModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pretend user is from china
        #self.fields["sensitive"].queryset = self.fields["sensitive"].queryset.filter(sites__in=[3])

    @property
    def language(self):
        return get_language()
