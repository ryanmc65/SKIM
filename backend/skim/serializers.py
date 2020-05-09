    # todo/serializers.py

from rest_framework import serializers
from .models import Skim

class SkimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skim
        fields = ('id', 'title')