import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kitap_pazari.settings')

import django
django.setup()
### Modellerimize ve django iceriklerine erismek icin yukaridaki ayarlamalari yapmamiz lazim.
### SIRALAMA COK ONEMLI

from django.contrib.auth.models import User

from faker import Faker
import requests

from kitaplar.api.serializers import KitapSerializer

fake = Faker(['en_US'])

def set_user():
    f_name = fake.first_name()
    l_name = fake.last_name()
    u_name = f'{f_name.lower()}_{l_name.lower()}'
    email = f'{u_name}@{fake.domain_name()}'
    print(f_name, l_name, email)

    user_check = User.objects.filter(username=u_name)

    while user_check.exists():
        u_name = u_name + str(random.randrange(1, 99))
        user_check = User.objects.filter(username=u_name)

    user = User(
        username = u_name,
        first_name = f_name,
        last_name = l_name,
        email = email,
        is_staff = fake.boolean(chance_of_getting_true=50),
    )

    user.set_password('testing321..')
    user.save()
    print('Kullanici kaydedildi', u_name)


from pprint import pprint

def kitap_ekle(konu):
    # url = 'https://openlibrary.org/search.json?q=love'
    url = 'https://openlibrary.org/search.json'
    payload = {'q': konu}
    response = requests.get(url, params=payload)

    if response.status_code != 200:
        print('Hatali istek yapildi:', response.status_code)
        return
    
    jsn = response.json()
    # pprint(jsn)

    # print(response.url)

    kitaplar = jsn.get('docs')

    for kitap in kitaplar:
        kitap_adi = kitap.get('title') 
        data = dict(
            isim = kitap_adi,
            yazar = kitap.get('author_name')[0], # birden fazla yazar gelirse ilk yazari al dedik.
            aciklama = '-'.join(kitap.get('author_name')),
            yayin_tarihi = fake.date_time_between(start_date='-10y', end_date='now', tzinfo=None),
        )
        # pprint(data)

        serializer = KitapSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print('Kitap kaydedildi: ', kitap_adi)
        else:
            continue