from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TestimonialViewSet, home

router = DefaultRouter()
router.register(r"testimonials", TestimonialViewSet, basename="testimonial")

urlpatterns = [
    path("", include(router.urls)),
    path("home/", home, name="home"),
]
