from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import gettext_lazy as _
from photologue.models import Photo, ImageModel, IMAGE_FIELD_MAX_LENGTH, get_storage_path

from parler.managers import TranslatableManager
from parler.models import TranslatableModel, TranslatedFields, TranslatableModelMixin


class Category(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_("Title"), max_length=200)
    )

    def __str__(self):
        return self.title


class Sensitive(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_("Title"), max_length=200)
    )
    sites = models.ManyToManyField(Site)

    def __str__(self):
        return self.title


class TranslatablePhoto(TranslatableModel, Photo):
    class Meta:
        proxy = True

    translations = TranslatedFields(
        xtitle = models.CharField(_("Title"), max_length=200, null=True, blank=True),
    )



class MyPhoto(TranslatableModelMixin, ImageModel):
    #class Meta:
    #    proxy = True

    translations = TranslatedFields(
        title = models.CharField(_("Title"), max_length=200),
        myimage = models.ImageField(
            _('My image'),
             max_length=IMAGE_FIELD_MAX_LENGTH,
             upload_to=get_storage_path
        )
    )

    objects = TranslatableManager()

    '''
    xdef __new__(cls, name, bases, attrs, **kwargs):
        import pdb;pdb.set_trace()
        super().__new__(name, bases, attrs, **kwargs)
        aaa = 1
    '''

    def __str__(self):
        return self.title

    def __getattribute__(self, name):
        try:
            if name == "image":
                return self.myimage
        except RuntimeError:
            pass
        return super().__getattribute__(name)


class MyModel(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_("Title"), max_length=200),
        category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL),
        sensitive = models.ForeignKey(Sensitive, blank=True, null=True, on_delete=models.SET_NULL),
        photos = models.ManyToManyField(MyPhoto),
        computed = models.CharField(_("Computed"), max_length=200, editable=False, null=True),
    )
    more_photos = models.ManyToManyField(MyPhoto)
    more_category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        #import pdb;pdb.set_trace()
        super().save(*args, **kwargs)
        aaa = 1

    def save_translation(self, translation, *args, **kwargs):
        #import pdb;pdb.set_trace()
        super().save_translation(translation, *args, **kwargs)
        translation.computed = self.title + translation.language_code
        translation.save()
        #aaa = 1
