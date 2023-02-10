from django.shortcuts import redirect


def url_check_home(self, request):
    if request.tenant.name == "public":
        return 'src.website.urls'
    return 'src.website.urls'
