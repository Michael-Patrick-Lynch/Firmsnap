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

    path("post/create", views.post_creation, name="create_post"),

    # The endpoint used during onboarding to create a new org after the
    # Stripe payement is recieved
    path("new_org", views.new_org, name="new_org"),

    path("admin", views.org_admin_panel, name="org_admin_panel"),
    path("admin/all_users", views.org_admin_all_users, name="org_admin_all_users"),
    path("admin/all_posts", views.org_admin_all_posts, name="org_admin_all_posts"),
    path("admin/all_comments", views.org_admin_all_comments, name="org_admin_all_comments"),

    path('admin/delete_comment/<int:pk>/', views.AdminDeleteComment.as_view(), name='admin_delete_comment'),
]
