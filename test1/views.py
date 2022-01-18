from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView , CreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import contactmodel
from .serializer import contactmodelserializer
from rest_framework.permissions import IsAuthenticated


class test(ListAPIView):
    queryset = contactmodel.objects.all()
    serializer_class = contactmodelserializer
    #permission_classes = (IsAuthenticated ,)

class create(CreateAPIView):
    queryset = contactmodel.objects.all()
    serializer_class = contactmodelserializer
    permission_classes = (IsAuthenticated,)

class personal(APIView):
    def get (self , request , pk):
        queryset = contactmodel.objects.get(pk = pk)
        serializer = contactmodelserializer(queryset)
        return Response(serializer.data)

    def delete (self , request , pk):
        queryset = contactmodel.objects.get(pk = pk)
        queryset.delete()
        return Response(status=201)

    def put(self , request , pk):
        queryset = contactmodel.objects.get(pk = pk)
        serializer = contactmodelserializer(queryset , request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=202)
        else:
            return Response(status=404)

    permission_classes = (IsAuthenticated ,)

class revoke(APIView):
    permission_classes = (IsAuthenticated ,)

    def delete(self , request):
        request.auth.delete()
        return Response(status=201)

