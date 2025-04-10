from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import MyUser, Notes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterUserSerializer(serializers.ModelSerializer):
    login = serializers.CharField(max_length=255, write_only=True, required=True, validators=[UniqueValidator(queryset=MyUser.objects.all())])
    name = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = MyUser
        fields = ('login', 'name', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'status': 'Passwords didnt match'})
        return attrs

    def create(self, validated_data):
        login = validated_data['login']
        password = validated_data['password']
        name = validated_data['name']
        user = MyUser.objects.create_user(login=login, name=name, password=password)
        return user


class NotesSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=1, max_length=255)
    discription = serializers.CharField()
    class Meta:
        model = Notes
        fields = ('id', 'title', 'discription')