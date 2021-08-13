"""parlerdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve

from parlerdemo import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('photologue/', include('photologue.urls', namespace='photologue')),
]

urlpatterns += i18n_patterns(
    path('mymodel/<int:pk>/change/', views.MyModelUpdateView.as_view(), name='mymodel-update'),
    path('mymodel/<int:pk>/', views.MyModelDetailView.as_view(), name='mymodel-detail'),
)

if settings.DEBUG:
    # Host our own media
    urlpatterns += [
        url(
            r"^media/(?P<path>.*)$",
            serve,
            {"document_root": settings.MEDIA_ROOT, "show_indexes": True}
        ),
    ]

