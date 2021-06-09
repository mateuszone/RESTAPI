from django.contrib.auth.models import User, Group
from rest_framework import serializers

from Api.models import Film, ExtraInfo, Review, Actor


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'required': True, 'write_only': True}}
        # za kazdym razem jak tworzymy nowego uzytkownika to haslo ktore podaje moze tylko wyslac,
        # nie wyswietli sie w responsie jsonowym i jest ustawione jako wymaganae

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        # if user:
        #     create authtoken
        # mozna tutaj standardowo stworzyc auth token dla nowego usera albo zrobic to bardziej zaawansowanie
        return user


class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = ['duration', 'genre']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        # object not subscriptable to np blad moze polegac na braku nawiasow okraglych a sa kwadratowe
        return instance
        # depth = 3
        # read_only_fields = ('film', 'id') zamiast dodawac do kazdego z osobna atrybut read_only mozna
        # to zrobic tutaj w fields
        # exclude = ['id',] albo to albo fields, nie mozna dwoch jednoczesnie


class FilmSerializer(serializers.ModelSerializer):
    extra_info = ExtraInfoSerializer(many=False)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Film
        fields = ['id', 'our_name', 'description', 'released',
                  'premiere', 'year', 'imdb_rating', 'extra_info', 'reviews']

        read_only_fields = ('extra_info', 'reviews')


class FilmMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['title', 'year']


class ActorSerializer(serializers.ModelSerializer):
    films = FilmMiniSerializer(many=True, read_only=True)

    # print(films)
    class Meta:
        model = Actor
        fields = ['id', 'name', 'surname', 'films']

# Daje mozliwosc tworzenia za pomocą raw json nowego aktora wraz z zagniezdzonym jsonem z filmami,
# wymaga wywalenia read_only=True z filmSerializer
# def create(self, validated_data):
#     print(validated_data)
#     films = validated_data['films']
#     del validated_data['films']
#
#     actor = Actor.objects.create(**validated_data)
#
#     for film in films:
#         f = Film.objects.create(**film)
#         actor.films.add(f)
#
#     actor.save()
#
#     return actor

# def create(self, validated_data):
#        profile_data = validated_data.pop('profile')
#        user = User.objects.create(**validated_data)
#        Profile.objects.create(user=user, **profile_data)
#        return user
