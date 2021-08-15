from django.db import models
from django.core.validators import MinLengthValidator


class User(models.Model):
    first_name = models.CharField(max_length=25, blank=False, default='')
    last_name = models.CharField(max_length=25, blank=False, default='')
    email_id = models.CharField(max_length=320, blank=False, default='', unique=True)
    contact_number = models.CharField(max_length=10, blank=False, default='', unique=True, validators=[MinLengthValidator(10)])
    permanent_address = models.CharField(max_length=100, blank=False, default='')
    education_qualification = models.CharField(max_length=25, blank=False, default='')
    active_status = models.CharField(max_length=10, blank=False, default='')
