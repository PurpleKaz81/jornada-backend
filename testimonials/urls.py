from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TestimonialViewSet

router = DefaultRouter()
router.register(r"testimonials", TestimonialViewSet, basename="testimonial")

urlpatterns = [
    path("", include(router.urls)),
]
