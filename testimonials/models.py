from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Testimonials(models.Model):
    photo = models.ImageField(upload_to="photos/")
    testimonial = models.TextField()
    name = models.CharField(max_length=200)

    photo_thumbnail = ImageSpecField(source="photo",
                                    processors=[ResizeToFill(100, 100)],
                                    format="JPEG",
                                    options={"quality": 60})
