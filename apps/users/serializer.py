from rest_framework import serializers
from apps.users.models import User
from apps.todo.serializers import ToDoSerializer
from django.core.validators import RegexValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 'last_name', 'date_joined', 'email')

class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length = 255, write_only=True
    )
    email = serializers.CharField(
        max_length = 255, write_only=True
    )
    phone_number = serializers.CharField(
        max_length = 255, write_only=True
    )
    age = serializers.IntegerField(
        write_only=True
    )
    password = serializers.CharField(
        max_length = 255, write_only=True
    )
    password2 = serializers.CharField(
        max_length = 255, write_only=True
    )

    class Meta:
        model = User 
        fields = ('username', 'email', 'phone_number', 'age', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли отличаются"})
        if '+996' not in attrs['phone_number']:
            raise serializers.ValidationError({"phone_number": "Напишите номер с +996"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email = self.initial_data.get("email"),
            phone_number = self.initial_data.get("phone_number"),
            age = self.initial_data.get("age"),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserDetailSerializer(serializers.ModelSerializer):
    user_todo = ToDoSerializer(read_only = True, many = True)
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 'last_name', 'date_joined', 'email', 'phone_number', 'created_at', 'age', 'user_todo')