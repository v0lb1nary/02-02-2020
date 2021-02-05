from django.db import models
from django.contrib.auth.models import User


class Familia(models.Model):

    mae = models.CharField(max_length = 50, blank = True)
    pae = models.CharField(max_length = 50, blank = True)

    class Meta:
        abstract = True


class Mixin(User, Familia):
    doce_preferido = models.CharField(max_length = 50)

    class Meta:
        """Meta definition for MODELNAME."""
        abstract = False
        verbose_name = 'Mixin'
        verbose_name_plural = 'Mixins'

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.get_full_name()
