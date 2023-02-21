from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import User



class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=50)
    email =serializers.EmailField(max_length=127 ,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="email already registered."
            )
            ]
    )
    username = serializers.CharField(max_length=127,
    validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="username already taken."
            )
            ])
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(required=False)
    password = serializers.CharField(write_only=True)
    is_employee = serializers.BooleanField(allow_null=True, default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    
    def create(self , validated_data:dict):
        employee = validated_data.get("is_employee")
        if employee:
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)        

    def update(self, instance: User, validated_data:dict) :
        for key , value in validated_data.items():
            setattr(instance , key , value)   
        new_password = validated_data.get("password")    
        instance.set_password(new_password)
        instance.save()

        return instance
