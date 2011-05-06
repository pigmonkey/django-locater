from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField, USStateField
from geopy import geocoders

class Location(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=500, blank=True)
    phone = PhoneNumberField()
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = USStateField()
    zip = models.CharField(max_length=5)
    lat = models.FloatField(editable=False)
    long = models.FloatField(editable=False)

    def __unicode__(self):
        return self.name

    @property
    def latlong(self):
        return (self.lat, self.long)

    @property
    def location(self):
        return '%s %s, %s %s' % (self.street_address, self.city, self.state, self.zip)

    def save(self, *args, **kwargs):
        # Geocode the address and save the lattitude and longitude
        g = geocoders.Google()
        latlong = g.geocode(self.location)[1]
        self.lat = latlong[0]
        self.long = latlong[1]
        # Call the real save
        super(Location, self).save(*args, **kwargs)
