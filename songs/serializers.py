from dataclasses import fields
from rest_framework import serializers
from .models import Songs

class SongsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Songs
        fields = "__all__"

    def create(self, validated_data):
        return Songs.objects.create(**validated_data)    