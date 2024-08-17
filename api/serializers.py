from rest_framework import serializers
from .models import Client, Project, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']


class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    # created_by = UserSerializer(required=False)

    class Meta:
        model = Client
        fields = ['id', 'name', 'created_at', 'created_by','updated_at']


class ProjectSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    users = UserSerializer(many=True)  # Use the updated UserSerializer
    created_by = serializers.StringRelatedField()
    

    class Meta:
        model = Project
        fields = ['id', 'name', 'client', 'users', 'created_at', 'created_by']
