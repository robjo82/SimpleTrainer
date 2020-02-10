from django.db.models import F
from .models import Stat


def stats_middleware(get_response):
    def middleware(request):
        try:
            p = Stat.objects.get(url=request.path)
            p.views_number = F("views_number") + 1
            p.save
        except Stat.DoesNotExist:
            p = Stat.objects.create(url=request.path)

        response = get_response(request)

        response.content += bytes(
            "cette page a été vue {} fois.".format(p.views_number), "utf8"
        )
        return response

    return middleware
