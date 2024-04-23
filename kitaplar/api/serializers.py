from rest_framework import serializers
from kitaplar.models import Kitap, Yorum


class YorumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yorum
        fields = '__all__'


class KitapSerializer(serializers.ModelSerializer):

    yorumlar = YorumSerializer(
        many = True, # birden fazla yorum oldugu icin bu satiri ekledik
        read_only = True, # yorum girmeden kitap eklenebilmesini saglar
    )
    class Meta:
        model = Kitap
        fields = '__all__'

