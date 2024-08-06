from django.urls import path

from .views import *

urlpatterns = [
    path('', Index.as_view(), name='main'),
    path('new_event/', NewEvent.as_view(), name='new_event_form'),
    path('new_author/', NewAuthor.as_view(), name='new_author_form'),
    path('all_posts/', AllPosts.as_view(), name='all_posts'),
    path('file_upload/', file_upload),
    path('<slug:slug>/', GetPostBySlug.as_view(), name='post_by_slug'),
]

