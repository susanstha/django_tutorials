# from django.contrib import admin
# from django.urls import path
# from . import views
# from blog.views import (PostListView,AboutView,
#                         PostDetailView,CreatePostView,
#                         PostUpdateView,PostDeleteView,DraftListView)


# urlpatterns = [
#     path('',PostListView.as_view(),name='post_list'),
#     path('about/',AboutView.as_View(), name='about' ),
#     path('post/(?P<pk>\d+)',PostDetailView.as_View(),name='post_detail'),
#     path('post/new/',CreatePostView.as_View(),name='post_new'),
#     path('post/(?P<pk>\d+)/edit/',PostUpdateView.as_View(),name='post_edit'),
#     path('post/(?P<pk>\d+)/remove/',PostDeleteView.as_View(),name='post_remove'),
#     path('drafts/',DraftListView.as_View(),name='post_draft_list'),
#     path('post/(?P<pk>\d+)/comment/',views.add_comment_to_post,name='add_comment_to_post'),
#     path('comment/(?P<pk>\d+)/approve/',views.comment_approve,name='comment_approve'),
#     path('comment/(?P<pk>\d+)/remove/',views.comment_remove,name='comment_remove'),
#     path('post/(?P<pk>\d+)/publish/',views.post_publish,name='post_publish'),
# ]

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]
