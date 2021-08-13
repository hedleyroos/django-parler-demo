from django.contrib import admin
from parler.admin import TranslatableAdmin, TranslatableTabularInline
from photologue.models import Photo

from parlerdemo import models


class PhotoInline(TranslatableTabularInline):
    model = Photo


class MyModelAdmin(TranslatableAdmin):
    #inlines = (PhotoInline,)
    pass


class CategoryAdmin(TranslatableAdmin):
    pass


class SensitiveAdmin(TranslatableAdmin):
    pass


class TranslatablePhotoAdmin(TranslatableAdmin):
    pass


class MyPhotoAdmin(TranslatableAdmin):
    pass


admin.site.register(models.MyModel, MyModelAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Sensitive, SensitiveAdmin)
admin.site.register(models.TranslatablePhoto, TranslatablePhotoAdmin)
admin.site.register(models.MyPhoto, MyPhotoAdmin)
