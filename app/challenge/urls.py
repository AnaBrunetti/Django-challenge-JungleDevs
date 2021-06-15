from .views import (
    UserCreateAPIView,
    ReactivateUser,
    DeactivateUser,
    CreateListAuthors,
    UpdateDeleteReadAuthor,
    CreateListArticles,
    UpdateDeleteReadArticle,
    ArticleView,
    ArticleDetail
)
from django.conf.urls import url

urlpatterns = [
    url(r'^sign-up/$', UserCreateAPIView.as_view(), name='create_user'),
    url(r'^reactivateUser/$', ReactivateUser.as_view(), name='reactivate_user'),
    url(r'^deactivateUser/$', DeactivateUser.as_view(), name='deactivate_user'),
    url(r'^admin/authors/$', CreateListAuthors.as_view(), name='create_list_authors'),
    url(r'^admin/authors/(?P<pk>[\w\-]+)/$', UpdateDeleteReadAuthor.as_view(), name='list_update_delete_author'),
    url(r'^admin/articles/$', CreateListArticles.as_view(), name='create_list_articles'),
    url(r'^admin/articles/(?P<pk>[\w\-]+)/$', UpdateDeleteReadArticle.as_view(), name='list_update_delete_article'),
    url(r'^articles/$', ArticleView.as_view(), name='list_articles'),
    url(r'^articles/(?P<pk>[\w\-]+)/$', ArticleDetail.as_view(), name='list_article_detail'),
   
]
