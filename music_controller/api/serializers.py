from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import Room


class RooomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause',
                  'votes_to_skip', 'created_at')
