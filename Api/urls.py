from django.urls import include, path
from rest_framework import routers
from Api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'films', views.FilmViewSet, basename="films")
router.register(r'reviews', views.ReviewViewSet, basename="reviews")
router.register(r'actors', views.ActorViewSet, basename="actors")

urlpatterns = [
    path('', include(router.urls)),
]

