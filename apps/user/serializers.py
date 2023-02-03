import re

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.user.models import User


# api/users/signup
class SignUpSerializer(ModelSerializer):
    def validate(self, data):
        password = data.get("password")
        regex_password = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,20}$"

        if not re.match(regex_password, password):
            raise serializers.ValidationError("문자, 숫자, 기호를 조합하여 8자 이상을 사용하세요.")

        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data.get("password"))
        user.save()

        return user

    class Meta:
        model = User
        fields = ["email", "password"]
        extra_kwargs = {"password": {"write_only": True}}
