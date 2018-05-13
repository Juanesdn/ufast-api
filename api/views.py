from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductsSerializer
from .models import Products


class CreateView(APIView):

    def get(self, request, format=None):
        queryset = Products.objects.all()
        serializer = ProductsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
