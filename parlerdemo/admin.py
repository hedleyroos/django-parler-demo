from django import forms
from django.contrib import admin
from parler.admin import TranslatableAdmin, TranslatableTabularInline
from parler.forms import TranslatableModelForm

from parlerdemo import models


class BlogAdmin(TranslatableAdmin):
    pass


class CategoryAdmin(TranslatableAdmin):
    pass


class SensitiveAdmin(TranslatableAdmin):
    pass


class MyPhotoAdminForm(TranslatableModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Change and hide the existing image field
        self.fields["image"].required = False
        self.fields["image"].widget = forms.HiddenInput()


class MyPhotoAdmin(TranslatableAdmin):
    form = MyPhotoAdminForm


admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Sensitive, SensitiveAdmin)
admin.site.register(models.MyPhoto, MyPhotoAdmin)
