from rest_framework.serializers import ModelSerializer
from .models import Resident, Flat, Bill, Item, Feedback, Survey, FaMember


class FlatSerializer(ModelSerializer):
    class Meta:
        model = Flat
        fields = ["id", "number", "floor"]

