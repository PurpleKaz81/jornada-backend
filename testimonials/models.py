from django.db import models

# Create your models here.

class Testimonials(models.Model):
    photo = models.ImageField(upload_to='testimonials')
    text = models.TextField()
    name = models.CharField(max_length=255)
