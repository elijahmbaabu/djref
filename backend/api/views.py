from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "Hello, this is your home page for Djago crash course!!"})