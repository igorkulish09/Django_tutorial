from .models import Log


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith("/admin"):
            log = Log(path=request.path, method=request.method)
            if request.method == "GET":
                log.request_data = request.GET.dict()
            elif request.method == "POST":
                log.request_data = request.POST.dict()
            log.save()

        response = self.get_response(request)
        return response
