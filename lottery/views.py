from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

def index (request):
    # Redirect to admin
    return redirect (reverse ('admin:index'))