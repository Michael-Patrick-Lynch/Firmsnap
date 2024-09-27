from django.urls import path

from . import views

urlpatterns = [
    # Ex: /app/
    path("", views.index, name="index"),

    # Ex: /app/post/1
    path("post/<int:post_id>", views.post_detail, name="post_detail"),

    # Ex: /app/all/1
    path("all/<int:organisation_id>", views.all_posts, name="all_posts"),
]