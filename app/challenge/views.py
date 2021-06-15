from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from .serializers import (
    UserSerializer,
    DeactivateUserSerializer, 
    ReactivateUserSerializer, 
    AdminAuthorSerializer,
    AdminArticleSerializer,
    ArticleSerializer,
    ArticleDetailSerializer
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .models import Author, Article

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]



class ReactivateUser(TokenObtainPairView):
    serializer_class = ReactivateUserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:  
            user = User.objects.get(username=request.data['username'])
            if (check_password(request.data['password'], user.password)):
                if user.is_active:
                    return Response(data='User already activate.')
                else:
                    user.is_active = True
                    user.save()
                    return Response(data='User activate.')
            else: 
                return Response(data='Incorrect password.')
        except Exception as e: 
            return Response(data=str(e))



class DeactivateUser(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    http_method_names = ['post']
    serializer_class = DeactivateUserSerializer

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(username=request.data['username'])
            if (check_password(request.data['password'], user.password)):
                user.is_active = False
                user.save()
                return Response(data='User deactivated.')
            else: 
                return Response(data='Incorrect password.')
        except Exception as e: 
            return Response(data=str(e))



class CreateListAuthors(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Author.objects.filter(is_active=True)
    serializer_class = AdminAuthorSerializer
    http_method_names = ['get', 'post']



class UpdateDeleteReadAuthor(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Author.objects.all()
    serializer_class = AdminAuthorSerializer
    http_method_names = ['get', 'put', 'patch', 'delete']



class CreateListArticles(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Article.objects.filter(is_active=True, author__is_active=True)
    serializer_class = AdminArticleSerializer
    http_method_names = ['get', 'post']



class UpdateDeleteReadArticle(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Article.objects.all()
    serializer_class = AdminArticleSerializer
    http_method_names = ['get', 'put', 'patch', 'delete']


class ArticleView(generics.ListAPIView):
    queryset = Article.objects.filter(is_active=True, author__is_active=True)
    http_method_names = ['get']

    def get(self, request, *args, **kwargs): 
        try:
            category = self.request.query_params.get('category', None)
            if category:
                queryset = Article.objects.filter(category=category, is_active=True, author__is_active=True)
                serializer_class = ArticleSerializer(queryset, many=True)
            else:
                serializer_class = ArticleSerializer(self.get_queryset(), many=True)
            return Response(data=serializer_class.data)
        except Exception as e:
            return Response(data=str(e))


class ArticleDetail(generics.RetrieveAPIView):
    http_method_names = ['get']

    def retrieve(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk')
            object = Article.objects.get(pk=kwargs['pk'])
            serializer = ArticleDetailSerializer(object, context={'request': request})
            return Response(data=serializer.data)
        except Exception as e:
            return Response(data=str(e))


