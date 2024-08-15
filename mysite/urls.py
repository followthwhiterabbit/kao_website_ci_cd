"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap

from django.conf.urls.static import static

from .sitemaps import MySitemap

sitemaps = {
    'my_sitemap': MySitemap,
}

urlpatterns = i18n_patterns(
    path("", include("about_page.urls")),
    path("polls/", include("polls.urls")), 
    path("contact/", include("contact_page.urls")),
    path("about/products", include("products_page.urls")),
    path("admin/", admin.site.urls),
    path("products/", include("products_page.urls") ),
    path("dimensionalmeasurement/", include("dimensional_measurement.urls")),
    path("leaktesting/", include("leak_testing.urls")),
    path("callibrators/", include("callibrators.urls")),
    path("accessories/", include("accessories.urls")),
    path("services/", include("services.urls")),
    path('rosetta/', include('rosetta.urls')), 
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
)

