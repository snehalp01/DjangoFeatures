from django.db import models

# Create your models here.

class Person(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)

class Musician(models.Model):
    musician = models.ForeignKey(Person, on_delete=models.CASCADE)
    instrument = models.CharField(max_length=20)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    lable_name = models.ForeignKey(RecordLabel, on_delete=models.PROTECT)

class RecordLabel(models.Model):
    lable_name = models.CharField(max_length=20)
    musicians = models.ManyToManyField(Musician, on_delete=models.CASCADE)

