from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):
    """Model referring to user profile,based on the top of django User model
    password-->
    reward-->points based on user activity
    address-->
    
    """
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    pw=models.CharField(max_length=10, blank=True)
    reward=models.IntegerField(blank=True,null=True)
    address = models.CharField(blank=True, max_length=300)
    verification_status_choices = (
        ('a', 'active'),
        ('d', 'deactive'),
        ('o', 'other'),
        ('p', 'pending'),
        ('s', 'suspended')
    )
    verification_status = models.CharField(blank=False, max_length=2, choices=verification_status_choices, default='p')
    verification_code = models.CharField(blank=False, max_length=128, default='123456')

    def __unicode__(self):
        return self.user.username

class Car(models.Model):
    """
    Model referring to the different cars of the users.
    """
    
    owner=models.ForeignKey(UserProfile)    #whose car
    registration_number=models.CharField(blank=True,null=True,max_length=300)   #car registration number
    car_model=models.CharField(blank=True,max_length=300,null=True) #which model
    number_of_seats=models.IntegerField(blank=True,null=True)       #how many seats
    #is the car available
    car_availablity_status_choices = (
        ('a', 'active'),
        ('d', 'deactive'),
        ('o', 'other'),
        ('p', 'pending'),
        ('s', 'suspended')
    )
    car_availablity_status = models.CharField(blank=False, max_length=2, choices=car_availablity_status_choices, default='p')
    
class Driver(models.Model):

    """
    Model referring to the different drivers of the owners.
    """

    driver_name=models.CharField(blank=True,null=True,max_length=50)
    driver_employer=models.ForeignKey(UserProfile)
    driver_address=models.CharField(blank=True,null=True,max_length=300)

class Location(models.Model):
    """
    Model referring to the different locations of the users.
    """
    location_name = models.CharField(blank=True, max_length=300)
    location_lat = models.FloatField(blank=True, null=True)
    location_long = models.FloatField(blank=True, null=True)

class Trip(models.Model):
    """
    Model referring to the different trips of the users.
    """

    source=models.ForeignKey(Location,related_name="source")
    destination=models.ForeignKey(Location,related_name="destination")
    driver_of_trip=models.ForeignKey(Driver)
    trip_time=models.DateTimeField(blank=True)

class TripRequest(models.Model):

    """
    Model referring to the different trip requests of the users.
    """

    user_requested=models.ForeignKey(UserProfile)
    trip_requested=models.ForeignKey(Trip)

class Ride(models.Model):
    """
    Model referring to the different rides of the users.
    """

    rider=models.ForeignKey(UserProfile)
    trip=models.ForeignKey(Trip)
