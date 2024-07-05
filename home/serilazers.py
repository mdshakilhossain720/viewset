from .models import Studetn
from rest_framework import serializers

class StudentSerilazer(serializers.ModelSerializer):
    class Meta:
        model=Studetn
        fields="__all__"
        