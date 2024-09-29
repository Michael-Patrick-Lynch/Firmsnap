from django.db import models

class Organisation(models.Model):
    org_name = models.CharField(max_length=200)

    def __str__(self):
        return self.org_name

class User(models.Model):
    organisation_id = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name

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
    
    comment_text = models.TextField(max_length=2000)
    pub_date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text
