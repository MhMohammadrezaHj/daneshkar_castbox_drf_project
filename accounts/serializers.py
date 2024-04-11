from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from djoser.serializers import UserSerializer as DjoserUserSerializer


class UserCreateSerializer(DjoserUserCreateSerializer):
    class Meta(DjoserUserCreateSerializer.Meta):
        fields = ["id", "username", "password", "email", "first_name", "last_name"]


class UserSerializer(DjoserUserSerializer):
    class Meta(DjoserUserSerializer.Meta):
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
        ]
        ref_name = "UserSerializerRefName"
