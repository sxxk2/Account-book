import uuid

from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView


class URLShortenerView(APIView):
    def random_url(self):
        return f"http://pay.here/{str(uuid.uuid4().int)[:10]}"

    def get(self, request):
        shorten_url = request.data["shorten_url"]
        original_url = cache.get(shorten_url)
        return Response({"original_url": original_url})

    def post(self, request):
        original_url = request.data["url"]
        shorten_url = self.random_url()
        cache.set(shorten_url, original_url, 1800)
        return Response({"shorten_url": shorten_url})
