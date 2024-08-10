
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class MySitemap(Sitemap):
    changefreq = "daily"
        

    def items(self):
        return ['about_page', 'products_page', 'dimensional_measurement', 'leak_testing', 'callibrators', 'accessories', 'services', 'contact_page']

    def location(self, item):
        return reverse(item)
