from django.shortcuts import render
from rest_framework import viewsets
from .models import Testimonial
from .serializers import TestimonialSerializer


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


def home(request):
    return render(request, "home.html")
