from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from apps.account_book.models import AccountBook
from apps.account_book.permissions import IsOwnerOrPostOnly
from apps.account_book.serializers import AccountBookSerializer


# api/account-books
class AccountBookView(ListCreateAPIView):
    permission_classes = [IsOwnerOrPostOnly]
    serializer_class = AccountBookSerializer

    def get_queryset(self):
        queryset = AccountBook.objects.filter(is_active=True, user=self.request.user)
        return queryset

    def create(self, request):
        serializer = self.get_serializer(data=request.data, context={"user": request.user})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
