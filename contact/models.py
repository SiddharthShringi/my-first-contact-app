from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=250)
    phone = PhoneNumberField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.full_name()
