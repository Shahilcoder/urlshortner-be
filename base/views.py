import json
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import render

from .models import Url
from .utils import shorten


# Create your views here.
@require_GET
def index(request):
    return JsonResponse({"message": "urlshortner api"})


@require_POST
@csrf_exempt
def generateShortUrl(request):
    jsonObj = json.loads(request.body)
    shortUrl = shorten(jsonObj["url"])

    try:
        Url.objects.create(long_url=jsonObj["url"], short_url=shortUrl)
    except:
        return JsonResponse({"error" : "An error occured while generating short url"}, status=500)

    return JsonResponse({"short": shortUrl})


@require_GET
def getLongUrl(request, url):
    try:
        url = Url.objects.get(short_url=url)
        # return JsonResponse({"url": url.long_url})
        return redirect(url.long_url)
    except:
        return JsonResponse({"message": "Not found"}, status=404)