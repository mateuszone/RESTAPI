from django.contrib.auth.models import User, Group
from rest_framework import viewsets, filters
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser, DjangoModelPermissions
from rest_framework.response import Response
from django.http.response import HttpResponseNotAllowed
from Api.models import Film, Review, Actor
from Api.serializers import UserSerializer, FilmSerializer, ReviewSerializer, ActorSerializer
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication

class FilmsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 7


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class FilmViewSet(viewsets.ModelViewSet):
    serializer_class = FilmSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ('title', 'description', 'year')
    search_fields = ('title', 'description')
    # ordering_fields = ('id', 'title', 'year')
    ordering_fields = "__all__"
    ordering = ('-year',)

    pagination_class = FilmsSetPagination
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated, )
    # permission_classes = (IsAdminUser, )
    permission_classes = (DjangoModelPermissions, )


    def get_queryset(self):
        # year = self.request.query_params.get('year', None)
        # id = self.request.query_params.get('id', None)
        # if id:
        #     film = Film.objects.filter(id=id)
        #     return film
        # else:
        #     if year:
        #         films = Film.objects.filter(year=year)
        #     else:
        films = Film.objects.all()
        return films

    # def list(self, request, *args, **kwargs):
    #     title = self.request.query_params.get('title', None)
    #
    #     # films = Film.objects.filter(title__exact=title)
    #     # films = Film.objects.filter(title__icontains=title)
    #     # films = Film.objects.filter(title__contains=title)
    #     # films = Film.objects.filter(year__lte=2000)
    #     # films = Film.objects.filter(year__gte=2000)
    #     # films = Film.objects.filter(premiere__gte="2000-01-01")
    #     films = Film.objects.filter(premiere__year__gte="2000")
    #
    #     # queryset = self.get_queryset()
    #
    #     # serializer = FilmMiniSerializer(queryset, many=True)
    #     serializer = FilmSerializer(films, many=True)
    #     return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = FilmSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # if request.user.is_staff:
        film = Film.objects.create(title=request.data['title'],
                                   description=request.data['description'],
                                   released=request.data['released'],
                                   year=request.data['year'])
        serializer = FilmSerializer(film, many=False)
        return Response(serializer.data)

    # else:
    #     return HttpResponseNotAllowed('Not allowed!')

    def update(self, request, *args, **kwargs):
        film = self.get_object()
        film.title = request.data['title']
        film.description = request.data['description']
        film.released = request.data['released']
        film.year = request.data['year']
        film.save()

        serializer = FilmSerializer(film, many=False)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        film = self.get_object()
        film.delete()
        return Response('Film was deleted')

    @action(detail=True)
    def released(self, request, **kwargs):
        film = self.get_object()
        film.released = True
        film.save()

        serializer = FilmSerializer(film, many=False)
        return Response(serializer.data)

    @action(detail=False)
    def release_all(self, request, **kwargs):
        film = Film.objects.all()
        film.update(released=True)

        serializer = FilmSerializer(film, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def before_release_all(self, request, **kwargs):
        film = Film.objects.all()
        film.update(released=False)

        serializer = FilmSerializer(film, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['POST'])
    def ultimate_release(self, request, **kwargs):
        film = Film.objects.all()
        film.update(released=request.data['released'])

        serializer = FilmSerializer(film, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    @action(detail=True, methods=['post'])
    def concat(self, request, **kwargs):
        actor = self.get_object()
        film = Film.objects.get(id=request.data['film'])
        actor.films.add(film)

        serializer = ActorSerializer(actor, many=False)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def remove(self, request, **kwargs):
        actor = self.get_object()
        film = Film.objects.get(id=request.data['film'])
        actor.films.remove(film)

        serializer = ActorSerializer(actor, many=False)
        return Response(serializer.data)
