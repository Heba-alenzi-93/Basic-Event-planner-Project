from rest_framework import serializers
from .models import EvenPlanner


class EvenPlannerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvenPlanner
        fields = "__all__"

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvenPlanner
        fields = "__all__"


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvenPlanner
        fields = "__all__"

        
class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvenPlanner
        fields = "__all__"