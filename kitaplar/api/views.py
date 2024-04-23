from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics

from kitaplar.api.serializers import KitapSerializer, YorumSerializer
from kitaplar.models import Kitap


class KitapListCreateAPIView(generics.ListCreateAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer


class KitapDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer



# class KitapListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    
#     queryset = Kitap.objects.all()
#     serializer_class = KitapSerializer

#     # Listelemek
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     # Olusturmak
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)