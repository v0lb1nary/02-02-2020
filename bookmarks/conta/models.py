from django.db import models
from django.contrib.auth.models import User

class Mixin(User):
    doce_preferido = models.CharField(max_length=50)
