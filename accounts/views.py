from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def profile_view(request):
    user = request.user
    if user.is_authenticated:
        return render(request, "registration/profile.html", {"user": user})
    else:
        return HttpResponse('You are not logged in')