from rest_framework import serializers
from .models import Webhook

class WebhookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Webhook
        fields="__all__"

# class WebhookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Webhook
#         fields=["time","content"]
