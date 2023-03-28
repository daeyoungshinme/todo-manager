from rest_framework import serializers
from .models import TodoManagerUser

class TodoManagerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoManagerUser
        fields = ('id_user','nm_user', 'email_user')