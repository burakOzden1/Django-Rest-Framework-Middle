from rest_framework import serializers
from kitaplar.models import Kitap, Yorum


class YorumSerializer(serializers.ModelSerializer):
    yorum_sahibi = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Yorum
        # fields = '__all__'
        exclude = ['kitap']


class KitapSerializer(serializers.ModelSerializer):

    yorumlar = YorumSerializer(
        many = True, # birden fazla yorum oldugu icin bu satiri ekledik
        read_only = True, # yorum girmeden kitap eklenebilmesini saglar
    )
    class Meta:
        model = Kitap
        fields = '__all__'

