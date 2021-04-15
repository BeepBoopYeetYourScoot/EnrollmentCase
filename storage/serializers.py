from rest_framework import serializers

from storage.models import Storage


class StorageSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели хранилища
    """
    cost = serializers.SerializerMethodField(source='get_cost', read_only=True)

    class Meta:
        model = Storage
        fields = [
            'title',
            'id',
            'amount',
            'unit',
            'price',
            'cost',
            'date'
        ]
        read_only = [
            'id',
            'cost'
        ]

    @staticmethod
    def get_cost(instance):
        """
        Метод для расчёта суммарной стоимости конкретного товара
        """
        cost = instance.amount * instance.price
        return cost
