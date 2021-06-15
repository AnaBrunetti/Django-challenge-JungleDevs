# from rest_framework import generics
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Author, Article
from bs4 import BeautifulSoup

def get_first_p(content):
    try:
        soup = BeautifulSoup(content)
        p = soup.p
        if p:
            return str(p)
        else:
            return 'Not found'
    except:
        return 'Not found'


def get_body(content):
    try:
        soup = BeautifulSoup(content)
        soup.p.decompose()
        return str(soup)
    except:
        return 'Not found'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password')

    def create(self, validated_data):
        try:
            user = super(UserSerializer, self).create(validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return user
        except Exception as e:
            return str(e)



class ReactivateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}
    )

    class Meta:

        model = User
        fields = ('username', 'password')
        http_method_names = ['post']



class DeactivateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}
    )

    class Meta:

        model = User
        fields = ('username', 'password')
        http_method_names = ['post']



class AdminAuthorSerializer(serializers.ModelSerializer):
    class Meta:

        model = Author
        fields = ('id', 'name', 'picture', 'additional_information', 'is_active')
        http_method_names = ['get', 'post', 'put', 'patch ', 'delete ']



class AdminArticleSerializer(serializers.ModelSerializer):
    class Meta:

        model = Article
        fields = ('id', 'author', 'category', 'title', 'summary', 'content', 'is_active')
        http_method_names = ['get', 'post', 'put', 'patch ', 'delete ']



class ArticleAuthorSerializer(serializers.ModelSerializer):
    class Meta:

        model = Author
        fields = ('id', 'name', 'picture')
        http_method_names = ['get']



class ArticleSerializer(serializers.ModelSerializer):
    author = ArticleAuthorSerializer(many=False, required=True)
    class Meta:

        model = Article
        fields = ('id', 'author', 'category', 'title', 'summary')
        http_method_names = ['get']


class ArticleDetailSerializer(serializers.ModelSerializer):
    author = ArticleAuthorSerializer(many=False, required=True)
    class Meta:

        model = Article
        fields = ('id', 'author', 'category', 'title', 'summary')
        http_method_names = ['get']

    def to_representation(self, instance):
        entry = super().to_representation(instance)
        entry['firstParagraph'] = get_first_p(instance.content)
        request = self.context.get('request')
        if request.user.is_authenticated:
            entry['body'] = get_body(instance.content)
        return entry

