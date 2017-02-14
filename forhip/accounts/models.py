from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    phone = models.CharField(max_length = 20,
    validators=[RegexValidator(r'^010[1-9]\d{7}$')])
    address = models.CharField(max_length=100)


# Create your models here.
