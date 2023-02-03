import re

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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


# api/users/signin
class SignInSerializer(TokenObtainPairSerializer):
    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)

            if not user.is_active:
                raise serializers.ValidationError("삭제된 계정입니다.")

            if not user.check_password(password):
                raise serializers.ValidationError("아이디 또는 비밀번호를 잘못 입력했습니다.")  # 비밀번호 틀림
        else:
            raise serializers.ValidationError("아이디 또는 비빌먼호를 잘못 입력했습니다.")  # 아이디 없음

        token = super().get_token(user)
        access_token = str(token.access_token)
        refresh_token = str(token)

        data = {
            "access": access_token,
            "refresh": refresh_token,
        }
        return data

    class Meta:
        model = User
        fields = ["email", "password"]
