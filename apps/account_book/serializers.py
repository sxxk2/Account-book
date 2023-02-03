from rest_framework.serializers import ModelSerializer

from apps.account_book.models import AccountBook


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
