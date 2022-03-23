from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        # fields = '__all__'
        exclude = ['id', 'user']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    link_resources = serializers.HyperlinkedRelatedField(
        many=True, view_name='link_resource-detail', read_only=True)
    snippets = serializers.HyperlinkedRelatedField(many=True,
                                                   view_name='snippet-detail',
                                                   read_only=True)
    profile = ProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'password', 'email', 'profile', 'link_resources', 'snippets', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        print(validated_data)
        user = User.objects.create(password=make_password(
            validated_data.pop('password')),
                                   **validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        print(validated_data)
        print(instance)
        profile = instance.profile
        validated_profile_data = validated_data['profile']
        profile.nickname = validated_profile_data.get('nickname',
                                                      profile.nickname)
        profile.gender = validated_profile_data.get('gender', profile.gender)
        profile.birthday = validated_profile_data.get('birthday',
                                                      profile.birthday)
        profile.avatar = validated_profile_data.get('avatar', profile.avatar)
        profile.address = validated_profile_data.get('address',
                                                     profile.address)
        profile.job = validated_profile_data.get('job', instance.job)
        profile.company = validated_profile_data.get('company',
                                                     profile.company)
        profile.description = validated_profile_data.get(
            'description', profile.description)
        instance.save()
        return instance
