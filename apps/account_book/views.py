from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from apps.account_book.models import AccountBook, AccountBookRecord
from apps.account_book.permissions import IsOwner
from apps.account_book.serializers import (
    AccountBookDeleteSerializer,
    AccountBookDetailSerializer,
    AccountBookRecordDeleteSerializer,
    AccountBookRecordDetailSerializer,
    AccountBookRecordSerializer,
    AccountBookRecordUpdateSerializer,
    AccountBookSerializer,
    AccountBookUpdateSerializer,
    DeletedAccountBookRestoreSerializer,
)


# api/account-books
class AccountBookView(ListCreateAPIView):
    permission_classes = [IsOwner]
    serializer_class = AccountBookSerializer

    def get_queryset(self):
        queryset = AccountBook.objects.filter(is_active=True, user=self.request.user)

        search = self.request.query_params.get("search")
        order = self.request.query_params.get("order")

        if search:
            queryset = queryset.filter(title__contains=search)
        if order == "recent":
            queryset = queryset.order_by("-created_at")
        elif order == "old":
            queryset = queryset.order_by("created_at")

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
class DeletedAccountBookRestoreOrHardDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    serializer_class = DeletedAccountBookRestoreSerializer
    allowed_methods = ["PATCH", "DELETE"]

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


class AccountBookRecordView(ListCreateAPIView):
    serializer_class = AccountBookRecordSerializer

    def get_queryset(self):
        queryset = AccountBookRecord.objects.filter(account_book=self.kwargs["pk"])
        return queryset

    def create(self, request, pk):
        account_book = get_object_or_404(AccountBook, pk=pk, is_active=True)

        if not account_book.user == request.user:
            return Response({"detail": "이 작업을 수행할 권한(permission)이 없습니다."}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.serializer_class(data=request.data, context={"account_book": account_book})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        account_book = get_object_or_404(AccountBook, pk=pk, is_active=True)

        if not account_book.user == request.user:
            return Response({"detail": "이 작업을 수행할 권한(permission)이 없습니다."}, status=status.HTTP_403_FORBIDDEN)

        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AccountBookRecordDetailView(RetrieveUpdateAPIView):
    permission_classes = [IsOwner]
    allowed_methods = ["GET", "PATCH", "DELETE"]

    def get_queryset(self):
        queryset = AccountBookRecord.objects.filter(pk=self.kwargs["record_pk"], is_active=True)
        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return AccountBookRecordDetailSerializer
        elif self.request.method == "PATCH":
            return AccountBookRecordUpdateSerializer
        elif self.request.method == "DELETE":
            return AccountBookRecordDeleteSerializer

    def get_object(self):
        filter_kwargs = {self.lookup_field: self.kwargs["record_pk"]}
        obj = get_object_or_404(self.get_queryset(), **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

    def delete(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
