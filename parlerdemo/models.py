from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import gettext_lazy as _
from photologue.models import ImageModel, IMAGE_FIELD_MAX_LENGTH, get_storage_path

from parler.managers import TranslatableManager
from parler.models import TranslatableModel, TranslatedFields, TranslatableModelMixin, TranslatedFieldsModel


class Category(TranslatableModel):
    translations = TranslatedFields(title=models.CharField(_("Title"), max_length=200))

    def __str__(self):
        return self.title


# The word Tibet may not appear in China. In future we may want to use the sites framework to limit
# vocabularies. It is not currently being used.
class Sensitive(TranslatableModel):
    translations = TranslatedFields(title=models.CharField(_("Title"), max_length=200))
    sites = models.ManyToManyField(Site)

    def __str__(self):
        return self.title


# A translatable photo. This illustrates how to convert a third party product to be translatable.
class MyPhoto(TranslatableModelMixin, ImageModel):
    translations = TranslatedFields(
        title=models.CharField(_("Title"), max_length=200),
        parler_image=models.ImageField(_("Image"), max_length=IMAGE_FIELD_MAX_LENGTH, upload_to=get_storage_path),
    )

    objects = TranslatableManager()

    def __str__(self):
        return self.title

    def __getattribute__(self, name):
        """The magic bit where we map existing fields to the translated fields."""
        try:
            if name == "image":
                return self.parler_image
        except RuntimeError:
            pass
        return super().__getattribute__(name)


class Blog(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Title"), max_length=200),
        category=models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL),
        sensitive=models.ForeignKey(Sensitive, blank=True, null=True, on_delete=models.SET_NULL),
        photos=models.ManyToManyField(MyPhoto, null=True, blank=True),
        computed=models.CharField(max_length=200, editable=False, null=True),
    )

    def __str__(self):
        return self.title

    def save_translation(self, translation, *args, **kwargs):
        """Overridden to set computed attribute."""
        super().save_translation(translation, *args, **kwargs)
        translation.computed = self.title + translation.language_code
        translation.save()
