from django.shortcuts import render

# Create your views here.
# purchase_orders/views.py
from rest_framework import generics
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
from .models import PurchaseOrder
from rest_framework.decorators import api_view, authentication_classes, permission_classes


class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    authentication_classes = [TokenAuthentication]  # Add TokenAuthentication
    permission_classes = [IsAuthenticated]  # Add IsAuthenticated permission
    

class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    authentication_classes = [TokenAuthentication]  # Add TokenAuthentication
    permission_classes = [IsAuthenticated]  # Add IsAuthenticated permission
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'PurchaseOrder deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    




@api_view(['POST'])
@authentication_classes([TokenAuthentication])  # Add this line
@permission_classes([IsAuthenticated])  # Add this line
def acknowledge_purchase_order(request, po_id):
    try:
        po = PurchaseOrder.objects.get(pk=po_id)
    except PurchaseOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        po.acknowledgment_date = datetime.now()
        po.save()
        return Response('Purchase order acknowledged', status=status.HTTP_200_OK)

# @api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication])  # Add this line
# @permission_classes([IsAuthenticated])  # Add this line
# def purchase_order_list(request):
#     if request.method == 'GET':
#         purchase_orders = PurchaseOrder.objects.all()
#         serializer = PurchaseOrderSerializer(purchase_orders, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PurchaseOrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication])  # Add this line
# @permission_classes([IsAuthenticated])  # Add this line
# def purchase_order_detail(request, po_id):
#     try:
#         po = PurchaseOrder.objects.get(pk=po_id)
#     except PurchaseOrder.DoesNotExist:
#         return Response({'error': 'Purchase order not found'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = PurchaseOrderSerializer(po)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = PurchaseOrderSerializer(po, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         po.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
