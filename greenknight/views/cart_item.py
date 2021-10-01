import logging
from ..models import CartItem, Cart
from ..serializers import CartItemSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def list(self, request):

        if request.session.get('cart_key'):
            try:
                cart = Cart.objects.get(cart_key=request.session.get('cart_key'))

                queryset = CartItem.objects.filter(cart=cart)
                serializer = CartItemSerializer(queryset, many=True)
            except Exception as e:
                logging.info("No cart available for product listing.")
                return Response({"message": "cart is empty"}, status=status.HTTP_204_NO_CONTENT)

        return Response({"cart": cart.cart_key, "cart_items": serializer.data})

    def retrieve(self, request, pk=None):
        queryset = CartItem.objects.all()
        supplier = get_object_or_404(queryset, pk=pk)
        serializer = CartItemSerializer(supplier)
        return Response(serializer.data)

    def destroy(self, request, pk):

        queryset = CartItem.objects.all()
        supplier = get_object_or_404(queryset, pk=pk)
        supplier.delete()
        return Response({"status": "deleted", "id": pk}, status=status.HTTP_204_NO_CONTENT)

    def create(self, request, pk=None):

        # create a cart and add to session
        if request.session.get('cart_key'):
            cart = Cart.objects.get(cart_key=request.session['cart_key'])
        else:
            cart = Cart()
            cart.save()
            request.session['cart_key'] = cart.cart_key

        cart_item_serializer = CartItemSerializer(data=request.data)
        cart_item_serializer.cart = cart

        if cart_item_serializer.is_valid():
            self.perform_create(cart_item_serializer)

            return Response({"id": cart_item_serializer.data['id'], "status": "created"},
                            status=status.HTTP_201_CREATED)
        return Response(cart_item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):

        queryset = CartItem.objects.all()
        supplier = get_object_or_404(queryset, pk=pk)
        serializer = CartItemSerializer(supplier, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)

            return Response({"id": serializer.data['id'], "name": serializer.data['name'],
                             "status": "updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


