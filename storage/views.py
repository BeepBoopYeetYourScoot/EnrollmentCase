from django.db.models import F, Sum
from rest_framework import status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from storage import serializers
from storage.models import Storage


class StorageViewSet(ModelViewSet):
    """
    Контроллер для обработки запросов и роутинга
    """
    queryset = Storage.objects.all()
    serializer_class = serializers.StorageSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):
        """
        Вывод списка всех имеющихся ресурсов
        """
        serializer = serializers.StorageSerializer(self.queryset, many=True)
        return Response(
            {
                'resources': serializer.data,
                'total_count': self.queryset.count()
            },
            status=status.HTTP_200_OK
        )


@api_view()
def total_cost(request):
    """
    Возвращает суммарную стоимость всех товаров на складе
    """
    summary = Storage.objects.aggregate(summary=Sum(F('amount') * F('price')))
    return Response(
        {'total_cost': summary},
        status=status.HTTP_200_OK
    )
