from rest_framework import serializers
from .models import Member

class Memberserializers(serializers.ModelSerializer):
    class Meta:
        model =Member
        fields=['name','memberId','bojId','bojsetLevel','bojsetGoal','bojLev']