from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from users.models import AppUser, BalanceHistory
from users.serializers import AppUserListSerializer, ModifyBalanceSerializer


class AppUserViewSet(ReadOnlyModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserListSerializer

    @action(methods=['post'], detail=True, serializer_class=ModifyBalanceSerializer)
    def modify_points(self, request, pk):
        instance = self.get_object()
        serializer = ModifyBalanceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        instance.balance += data['amount']
        instance.save()
        BalanceHistory.objects.create(user=instance, amount=data['amount'], event_type=data['event_type'])
        return Response(AppUserListSerializer(instance=instance).data)
