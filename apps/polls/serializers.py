#  _*_ coding:UTF-8 _*_
from apps.polls.models import Man_Model
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class ManSerializer(serializers.ModelSerializer):
    class Meta:
        model = Man_Model
        fields = ('name', 'age')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
