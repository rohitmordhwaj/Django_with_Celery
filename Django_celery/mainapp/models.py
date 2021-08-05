from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=50, default= '')
    pizzas = models.ManyToManyField(Pizza, related_name='restaurants')
    best_pizza = models.ForeignKey(Pizza, related_name='championed_by', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='London')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)

    objects = models.Manager()
    london = UserProfileManager()

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    print("sender is ",sender)
    print(kwargs)
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)