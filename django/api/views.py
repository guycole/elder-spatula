from django.shortcuts import render

from django.http import HttpResponse

from rest_framework import permissions, viewsets

from .models import Simple
from .serializers import SimpleSerializer

class SimpleViewSet(viewsets.ModelViewSet):
    queryset = Simple.objects.all().order_by('key')
    serializer_class = SimpleSerializer
    permission_classes = [permissions.IsAuthenticated]