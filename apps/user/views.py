from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import BlacklistedToken, OutstandingToken, RefreshToken

from apps.user.serializers import SignInSerializer, SignUpSerializer


# api/users/signup
class SignUpView(APIView):
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "회원가입에 성공했습니다."},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


# api/users/signin
class SignInView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignInSerializer(data=request.data)

        if serializer.is_valid():
            token = serializer.validated_data
            return Response(
                {
                    "message": "로그인 되었습니다.",
                    "access_token": token["access"],
                    "refresh_token": token["refresh"],
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


# api/users/signout
class SignOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        try:
            refresh_token = RefreshToken(request.data["refresh_token"])
        except:
            return Response({"message": "유효하지 않거나 만료된토큰입니다."}, status=status.HTTP_400_BAD_REQUEST)

        if user.id != refresh_token["user_id"]:
            return Response({"message": "다른유저의 토큰입니다."}, status=status.HTTP_400_BAD_REQUEST)

        for token in OutstandingToken.objects.filter(token=refresh_token):
            BlacklistedToken.objects.create(token=token)

        return Response({"message": "로그아웃 되었습니다."}, status=status.HTTP_200_OK)
