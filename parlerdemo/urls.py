from django.conf import settings
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve

from parlerdemo import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path("photologue/", include("photologue.urls", namespace="photologue")),
]

urlpatterns += i18n_patterns(
    path("blog/<int:pk>/change/", views.BlogUpdateView.as_view(), name="blog-update"),
    path("blog/<int:pk>/", views.BlogDetailView.as_view(), name="blog-detail"),
)

if settings.DEBUG:
    # Host our own media
    urlpatterns += [
        url(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT, "show_indexes": True}),
    ]
