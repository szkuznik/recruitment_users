from rest_framework import serializers

from users.models import AppUser, BalanceHistory


class AppUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        exclude = ['referrer_email']


class ModifyBalanceSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=AppUser.objects.all())
    amount = serializers.IntegerField()
    event_type = serializers.ChoiceField(choices=BalanceHistory.TYPES)

    class Meta:
        fields = ['user', 'amount', 'event_type']

