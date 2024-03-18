from rest_framework import serializers


class NumbersSerializer(serializers.Serializer):
    data = serializers.ListField(child=serializers.IntegerField(), required=True)

    def validate_data(self, data):
        if not data:
            raise serializers.ValidationError(f"You can't send an empty list")
        return data
