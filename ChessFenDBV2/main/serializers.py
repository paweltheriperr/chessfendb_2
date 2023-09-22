from rest_framework import serializers
from .models import Fen


class FenSerializer(serializers.Serializer):
    fen = serializers.CharField(required=True, allow_blank=True, max_length=255)
    user = serializers.CharField(max_length=50, required=False)
    debiut_name = serializers.CharField(max_length=255)

    added = serializers.DateTimeField(required=True)

    def create(self, validated_data):
        return Fen.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.fen = validated_data.get('fen', instance.fen)
        instance.user = validated_data.get('user', instance.user)
        instance.debiut_name = validated_data.get('debiut_name', instance.debiut_name)
        instance.added = validated_data.get('added', instance.added)

        instance.save()

        return instance
