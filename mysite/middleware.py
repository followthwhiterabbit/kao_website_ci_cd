# mysite/middleware.py
import logging
from django.http import HttpResponsePermanentRedirect
from django.conf import settings

logger = logging.getLogger(__name__)

class RedirectToWWWMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        logger.debug(f"Host: {host}")

        if not host.startswith('www.') and not settings.DEBUG:
            new_url = request.build_absolute_uri().replace(host, f'www.{host}')
            logger.debug(f"Redirecting to: {new_url}")
            return HttpResponsePermanentRedirect(new_url)


        if host.startswith('https://') and not settings.DEBUG:
            new_url = request.build_absolute_uri().replace(host, f'https://www.{host}')
            logger.debug(f"Redirecting to: {new_url}")
            return HttpResponsePermanentRedirect(new_url)



        
        response = self.get_response(request)
        return response
