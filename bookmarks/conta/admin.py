from django.contrib import admin
from .models import Mixin

@admin.register(Mixin)
class MixinAdmin(admin.ModelAdmin):
    '''Admin View for Mixin'''

    list_display = ('username','doce_preferido',)
    list_filter = ('first_name',)
  