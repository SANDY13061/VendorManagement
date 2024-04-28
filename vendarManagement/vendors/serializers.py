# vendors/serializers.py
from rest_framework import serializers
from .models import Vendor
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
        
    def create(self, validated_data):
        # Hash the password before saving the user
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)