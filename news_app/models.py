from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from time import time

# Create your models here.

class Article(models.Model):
   title = models.CharField(max_length=200)
   body = models.TextField()
   pub_date = models.DateTimeField(auto_now=True)
   likes = models.IntegerField(default=0)
   username = models.ForeignKey('auth.User')

   def __unicode__(self):
        return unicode(self.title)
    
   def _unicode_(self):
	      return unicode(self.username)


        

class Brickout(models.Model):
  score = models.DecimalField(max_digits=4, decimal_places=0)

  def getScore(self):
      return self.score  
      
      
      
#class Likes(models.Model):
#    liker = models.ForeignKey(User)
#    link = models.ForeignKey(Link)
      
      
      
      
      
class Messages(models.Model):
   title = models.CharField(max_length=200)
   message = models.TextField()
   viewed = models.BooleanField(default=False)
   user = models.ForeignKey(User) 
   
   
   
   
   
@receiver(post_save, sender=User)
def create_message(sender, **kwargs):
    if kwargs.get('created', False):
        Messages.objects.create(user=kwargs.get('instance'), title="Welcome to News 'n Stuff!!", message="Thank you for joining our site!")   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
      
      
      
      
      
      
      
      
      
