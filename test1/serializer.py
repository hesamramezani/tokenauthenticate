from rest_framework import serializers
from .models import contactmodel
from django.contrib.auth.models import User

class contactmodelserializer(serializers.ModelSerializer):
    class Meta:
        model = contactmodel
        fields = "__all__"
