from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Triive AI")