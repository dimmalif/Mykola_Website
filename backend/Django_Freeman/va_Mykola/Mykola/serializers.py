from rest_framework import serializers

from Mykola.models import Users


class MykolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('person_email')
