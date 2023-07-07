from rest_framework import serializers
from .models import Testimonial

class TestimonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"
