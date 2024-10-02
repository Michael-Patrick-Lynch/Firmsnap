from django.urls import path

from . import views

urlpatterns = [
    # Ex: /app/
    path("", views.index, name="index"),

    # Ex: /app/post/1
    path("post/<int:post_id>", views.post_detail, name="post_detail"),

    # Ex: /app/all
    # Shows all the posts for the org of the user making the requests
    path("all", views.all_posts, name="all_posts"),

    path("post/create", views.post_creation, name="create_post")
]