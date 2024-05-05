from django.shortcuts import render

from django.http import HttpResponse

from .models import Simple
from rest_framework import permissions, viewsets

from .serializers import SimpleSerializer

def index(request):
    return HttpResponse("demo index")

class SimpleViewSet(viewsets.ModelViewSet):
    queryset = Simple.objects.all().order_by('key')
    serializer_class = SimpleSerializer
    permission_classes = [permissions.IsAuthenticated]