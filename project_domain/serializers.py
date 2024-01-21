from rest_framework import serializers
from project_domain.models import YourModel

class YourModelSerializer(serializers.Serializer):
    tableId = serializers.CharField()
    createdDatetime = serializers.CharField()

    def to_representation(self, instance):
        """
        Convert the model instance to a dictionary.
        """
        return {
            'tableId': instance.tableId,
            'createdDatetime': instance.createdDatetime,
        }

    def to_internal_value(self, data):
        """
        Convert the dictionary to a model instance.
        """
        return YourModel(**data)
