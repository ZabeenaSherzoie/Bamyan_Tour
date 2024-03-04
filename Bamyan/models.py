from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class TourAgency(models.Model):
    """
    Tour agency model to add information about the agency, give
    description of its services and its location.
    """
    name = models.CharField(max_length=50, blank=False)
    Location = models.CharField(max_length=50, blank=False)
    description = models.TextField(
        blank=True, help_text='Warning editing this'
        'field will change the About Us section on the home page!')

    def __str__(self):
        return self.name


class Season(models.Model):
    """
    Season model to add the name of season in
    which the packages will be available, and the information about when
    a season starts and ends.
    """
    name = models.CharField(max_length=10, blank=False)
    start = models.CharField(max_length=15,blank=False)
    end = models.CharField(max_length=15,blank=False)
    description = models.TextField(
        blank=False, default="No description is provided!")

    def __str__(self):
        return self.name


class Package(models.Model):
    """
    Packages model to add information about packages, the seasons they
    are available,the start place, duration etc.
    """
    PSIZES = ((2, "small"), (4, "medium"), (8, "Large"))
    season = models.ForeignKey(
        Season, on_delete=models.CASCADE, related_name='packages')
    title = models.CharField(max_length=100, blank=False)
    featured_image = CloudinaryField('image', default='placeholder')
    duration = models.CharField(max_length=50, default="3 days",blank=False)
    start_place = models.CharField(max_length=50,blank=False)
    end_place = models.CharField(max_length=50, blank=False)
    package_size = models.IntegerField(choices=PSIZES, default=2)
    description = models.TextField(
        blank=False, default="No description is provided!")
    

    def __str__(self):
        return self.title


