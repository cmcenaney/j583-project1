from django.db import models

# Create your models here.
class Players(models.Model):
    name = models.CharField(unique=False, max_length=50)
    number = models.CharField(unique=False, max_length=12)
    position  = models.CharField(unique=False, max_length=12)
    height = models.IntegerField(unique=False, max_length=3)
    weight = models.IntegerField(unique=False, max_length=50)
    year  = models.CharField(unique=False, max_length=12)
    hometown = models.CharField(unique=False, max_length=3)
    high_school = models.CharField(unique=False, max_length=50)
    major = models.CharField(unique=False, max_length=12)
    
    #imageurl = models.ImageField(max_length = 100)
    class Meta(object):
        verbose_name_plural = "Players"
        #ordering = ('-date', 'name',)
        
    def __unicode__(self):
        return U'%s' %(self.name)

class Team(models.Model):
    name = models.CharField(unique=True, max_length=50)
    season = models.CharField(unique=True, max_length=4)
    record = models.CharField(unique=True, max_length=50)
    players = models.ManyToManyField(Players)
    
   
    def __unicode__(self):
        return U'%s' %(self.name)
    
    #def save(self, *args, **kwargs):
        #self.name = self.name.upper()
        #super(Course, self).save(*args, **kwargs)