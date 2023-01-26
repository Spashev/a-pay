from django.http import HttpRequest
from django.contrib.sites.shortcuts import get_current_site


def get_domain(request: HttpRequest) -> str:
    current_site = get_current_site(request)
    domain_name = current_site.domain
    protocol = 'https://' if request.is_secure() else 'http://'
    return protocol + domain_name
