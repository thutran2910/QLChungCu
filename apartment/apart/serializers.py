from rest_framework.serializers import ModelSerializer
from .models import Resident, Flat, Bill, Item, Feedback, Survey, FaMember


class ResidentSerializer(ModelSerializer):
    class Meta:
        model = Resident
        fields = ["email", "username", "password", "avatar"]
        extra_kwargs = {
            'password': {'write_only': 'true'}
        }

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = instance.image.url
        return rep

    def create(self, validated_data): # đăng kí
        resident = Resident(**validated_data)
        resident.set_password(validated_data['password'])
        resident.save()
        return resident

class FlatSerializer(ModelSerializer):
    class Meta:
        model = Flat
        fields = '__all__'

class BillSerializer(ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class SurveySerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'

class FaMemberSerializer(ModelSerializer):
    class Meta:
        model = FaMember
        fields = '__all__'