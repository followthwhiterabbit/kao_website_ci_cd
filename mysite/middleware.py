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
        scheme = request.scheme
        logger.debug(f"Host: {host}, Scheme: {scheme}")


        #if not host.startswith('www.') and not settings.DEBUG:
            #new_url = request.build_absolute_uri().replace(host, f'www.{host}')
            #logger.debug(f"Redirecting to: {new_url}")
            #return HttpResponsePermanentRedirect(new_url)
        
        # Ensure https with www
        if scheme == 'https' and not host.startswith('www.') and not settings.DEBUG:
            new_url = request.build_absolute_uri().replace(host, f'www.{host}')
            logger.debug(f"Redirecting to: {new_url}")
            return HttpResponsePermanentRedirect(new_url) 

         #Redirect any non-www request to www, maintaining the scheme
        if not host.startswith('www.') and not settings.DEBUG:
            new_host = f'www.{host}'
            new_url = request.build_absolute_uri().replace(host, new_host)
            logger.debug(f"Redirecting to: {new_url}")
            return HttpResponsePermanentRedirect(new_url)   


        
        
        response = self.get_response(request)
        return response
