from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta
from django.utils import timezone

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Experience_CHOICES = (
        ("None","None"),
        ("Some","Some"),
        ("Good","Good"),
        ("Extensive","Extensive")
    )
    Goal_CHOICES = (
        ('Major Savings','Saving for major expenses or purchase (education, vacation, debt etc.) '),
        ('Wealth','Building long term wealth and preparing for retirement'),
        ('Testing','Testing the digital currency market.')
    )
    Portfolio_CHOICES = (
        ('M','Momentum'),
        ('C','Consecutive')
    )

    withdrawdate = models.DateField(default= timezone.now() + timedelta(days=30) )
    goal = models.CharField(max_length=500,
                            choices=Goal_CHOICES,
                            blank=True,
                            default='Testing the digital currency market.')
    portfolio = models.CharField(max_length=100,
                                 choices=Portfolio_CHOICES,
                                 blank=True,
                                 default='Consecutive')
    investmentAmount = models.DecimalField(decimal_places=2,
                                           max_digits=12,
                                           default=1,
                                           blank=True)
    currency_understand = models.CharField(max_length=20,
                                           choices=Experience_CHOICES,
                                           blank=True,
                                           default="Good")


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=kwargs.get('instance'))
