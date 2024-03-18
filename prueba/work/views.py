from rest_framework.views import APIView
import requests
from work.serializers import NumbersSerializer
from statistics import median
from rest_framework.response import Response
import math


class NumbersView(APIView):
    serializer_class = NumbersSerializer

    def post(self, request):
        serializer = NumbersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data["data"]
        suma = sum(validated_data)
        items = len(validated_data)
        payload = {
            "min": min(validated_data),
            "max": max(validated_data),
            "average": suma / items,
            "med": math.floor(median(validated_data)),
        }
        return Response(payload)
