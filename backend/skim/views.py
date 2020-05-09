from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import SkimSerializer      # add this
from .models import Skim                   # add this

class SkimView(viewsets.ModelViewSet):       # add this
    serializer_class = SkimSerializer          # add this
    queryset = Skim.objects.all()              # add this