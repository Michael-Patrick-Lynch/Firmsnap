from django.db import models
from django.contrib.auth.models import AbstractUser


class Organisation(models.Model):
    org_name = models.CharField(max_length=200)
    seats_remaining = models.IntegerField()  # Based on their current subscription
    seats_paid_for = models.IntegerField()

    def __str__(self):
        return self.org_name


class User(AbstractUser):
    organisation_id = models.ForeignKey(
        Organisation, on_delete=models.CASCADE, null=True, blank=True
    )
    is_org_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    organisation_id = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=200, default="Untitled Post")
    post_text = models.TextField(max_length=2000)
    pub_date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.post_title


class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    organisation_id = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    comment_text = models.TextField(max_length=2000)
    pub_date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text
