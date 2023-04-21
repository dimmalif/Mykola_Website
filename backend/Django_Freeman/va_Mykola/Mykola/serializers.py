from rest_framework import serializers

from .models import *


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ('id', 'features_name')
