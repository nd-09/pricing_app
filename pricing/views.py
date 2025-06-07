from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PriceCalculationSerializer
from .services import calculate_price

class CalculatePriceAPIView(APIView):
    def post(self, request):
        serializer = PriceCalculationSerializer(data=request.data)
        if serializer.is_valid():
            result = calculate_price(serializer.validated_data)
            if 'error' in result:
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
