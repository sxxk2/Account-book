from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.response import Response

from apps.account_book.models import AccountBook
from apps.account_book.permissions import IsOwner, IsOwnerOrPostOnly
from apps.account_book.serializers import (
    AccountBookDeleteSerializer,
    AccountBookDetailSerializer,
    AccountBookSerializer,
    AccountBookUpdateSerializer,
    DeletedAccountBookRestoreSerializer,
)


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

    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# api/account-books/deleted
class DeletedAccountBookView(ListAPIView):
    permission_classes = [IsOwner]
    serializer_class = AccountBookSerializer

    def get_queryset(self):
        queryset = AccountBook.objects.filter(is_active=False, user=self.request.user)
        return queryset


# api/account-books/deleted/<int:pk>
class DeletedAccountBookRestoreView(UpdateAPIView):
    permission_classes = [IsOwner]
    serializer_class = DeletedAccountBookRestoreSerializer
    allowed_methods = ["PATCH"]

    def get_queryset(self):
        queryset = AccountBook.objects.filter(is_active=False, pk=self.kwargs["pk"])
        return queryset


# api/account-books/<int:pk>
class AccountBookDetailView(RetrieveUpdateAPIView):
    permission_classes = [IsOwner]
    allowed_methods = ["GET", "PATCH", "DELETE"]

    def get_queryset(self):
        queryset = AccountBook.objects.filter(pk=self.kwargs["pk"])
        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return AccountBookDetailSerializer
        elif self.request.method == "PATCH":
            return AccountBookUpdateSerializer
        elif self.request.method == "DELETE":
            return AccountBookDeleteSerializer

    def retrieve(self, request, *args, **kwargs):
        account_book = self.get_object()
        serializer = self.get_serializer(account_book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
