from datetime import datetime

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.account_book.models import AccountBook, AccountBookRecord


# api/account-books
class AccountBookSerializer(ModelSerializer):
    def create(self, validated_data):
        user = self.context["user"]

        account_book = AccountBook.objects.create(user=user, **validated_data)
        account_book.save()

        return account_book

    class Meta:
        model = AccountBook
        exclude = [
            "deleted_at",
            "updated_at",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "user": {"read_only": True},
            "is_active": {"read_only": True},
        }


# api/account-books/deleted/<int:pk>
class DeletedAccountBookRestoreSerializer(ModelSerializer):
    def update(self, instance, validated_data):
        instance.is_active = True
        instance.deleted_at = None
        instance.updated_at = datetime.now()
        instance.save()

        return instance

    class Meta:
        model = AccountBook
        fields = [
            "is_active",
            "deleted_at",
            "updated_at",
        ]
        extra_kwargs = {"id": {"read_only": True}}


# api/account-books/<int:pk>
class AccountBookDetailSerializer(ModelSerializer):
    class Meta:
        model = AccountBook
        exclude = [
            "deleted_at",
        ]
        extra_kwargs = {"id": {"read_only": True}}


# api/account-books/<int:pk>
class AccountBookUpdateSerializer(ModelSerializer):
    def validate(self, data):
        if not data:
            raise serializers.ValidationError("입력값이 없습니다.")
        return data

    def update(self, instance, validated_data):
        account_book = super().update(instance, validated_data)
        account_book.updated_at = datetime.now()
        account_book.save()

        return account_book

    class Meta:
        model = AccountBook
        fields = [
            "id",
            "title",
            "balance",
            "updated_at",
        ]
        extra_kwargs = {"id": {"read_only": True}}


# api/account-books/<int:pk>
class AccountBookDeleteSerializer(ModelSerializer):
    def update(self, instance, validated_data):
        if not instance.is_active:
            raise serializers.ValidationError("이미 삭제된 가계부 입니다.")

        instance.is_active = False
        instance.deleted_at = datetime.now()
        instance.save()

        return instance

    class Meta:
        model = AccountBook
        fields = [
            "id",
            "is_active",
            "deleted_at",
        ]
        extra_kwargs = {"id": {"read_only": True}}


# api/account-books/<int:pk>/records
class AccountBookRecordSerializer(ModelSerializer):
    def create(self, validated_data):
        account_book = self.context["account_book"]

        account_book_record = AccountBookRecord.objects.create(account_book=account_book, **validated_data)
        account_book_record.save()

        return account_book_record

    class Meta:
        model = AccountBookRecord
        exclude = [
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "account_book": {"read_only": True},
            "is_active": {"read_only": True},
        }


# api/account-books/<int:pk>/records/record_pk
class AccountBookRecordDetailSerializer(ModelSerializer):
    class Meta:
        model = AccountBookRecord
        exclude = [
            "deleted_at",
        ]
        extra_kwargs = {"id": {"read_only": True}}


# api/account-books/<int:pk>/records/record_pk
class AccountBookRecordUpdateSerializer(ModelSerializer):
    def validate(self, data):
        if not data:
            raise serializers.ValidationError("입력값이 없습니다.")
        return data

    def update(self, instance, validated_data):
        account_book_record = super().update(instance, validated_data)
        account_book_record.updated_at = datetime.now()
        account_book_record.save()

        return account_book_record

    class Meta:
        model = AccountBookRecord
        fields = [
            "id",
            "amount",
            "description",
            "updated_at",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "account_book": {"read_only": True},
        }


class AccountBookRecordDeleteSerializer(ModelSerializer):
    def update(self, instance, validated_data):
        if not instance.is_active:
            raise serializers.ValidationError("이미 삭제된 메모 입니다.")

        instance.is_active = False
        instance.deleted_at = datetime.now()
        instance.save()

        return instance

    class Meta:
        model = AccountBook
        fields = [
            "id",
            "is_active",
            "deleted_at",
        ]
        extra_kwargs = {"id": {"read_only": True}}
