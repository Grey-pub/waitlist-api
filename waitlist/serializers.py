from rest_framework import serializers
from .models import Waitlist


class RecieveWaitlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waitlist
        exclude = ("response", "responded",  "time_created")


class ViewWaitlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waitlist
        fields = "__all__"

class RespondWaitlistSerializer(serializers.ModelSerializer):
    response = serializers.CharField(required=True)
    
    class Meta:
        model = Waitlist
        fields = "__all__"
        read_only_fields = ("id", "firsT_name", "last_name", "email", "question")
