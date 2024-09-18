from rest_framework import serializers
from .models import User

# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=100)
#     age = serializers.IntegerField()
#     mobile = serializers.CharField(max_length=10)
#     email = serializers.EmailField()
#     country = serializers.CharField(max_length=20)

    # def validate_username(self, value):
    #     if 'steve' not in value.lower():
    #         raise serializers.ValidationError("username must be contain steve")
    #     return value

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'