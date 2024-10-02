import logging
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from app.forms import PostCreationForm, CommentCreationForm
from .models import Post, Comment
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse

def index(request):
    return redirect('all_posts')

def post_detail(request, post_id):
    user = request.user
    post_obj = get_object_or_404(Post, id=post_id)

    # You can only view posts from your own organisation
    if user.is_authenticated and user.organisation_id == post_obj.organisation_id:
        if request.method == 'POST':
            comment_form = CommentCreationForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.user_id = request.user
                new_comment.post_id = Post.objects.get(pk=post_id)

                new_comment.save()
                return redirect('post_detail', post_id=post_id)
        else:
            comment_form = CommentCreationForm()

        list_of_comments = Comment.objects.filter(post_id=post_id)
        template = loader.get_template("app/post_detail.html")
        context = {"post_obj" : post_obj, "list_of_comments": list_of_comments,'comment_form': comment_form, 'post_id':post_id}
        return HttpResponse(template.render(context, request))
    else:
        return redirect('login')


# All posts from the users organisation
def all_posts(request):
    user = request.user

    if user.is_authenticated and user.organisation_id:
        organisation_id = user.organisation_id
        list_of_posts = Post.objects.filter(organisation_id=organisation_id)
        return render(request, "app/all_posts.html", {"list_of_posts": list_of_posts})
    else:
        return redirect('login')

def post_creation(request):
    # If we hit this view with a POST request, we try
    # to create a new post based on the form input
    if request.method == "POST":
        form = PostCreationForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)

            # Fill in the fields of the new post with context from the request
            new_post.user_id = request.user
            new_post.organisation_id = request.user.organisation_id
            new_post.save()

            return HttpResponseRedirect("/") # This should direct us to view the created post
    else:
        # If we hit this view with a GET request, we return the form
        form = PostCreationForm()

    return render(request, "app/post_creation.html", {"form": form})

# This is needed so that users are directed to the feed for
# their org as soon as they log in
class CustomLoginView(LoginView):
    def get_redirect_url(self):
        user = self.request.user

        # If the login is not working, it could be because the user has no org id!!
        if user.is_authenticated and user.organisation_id:
            redirect_url = reverse('all_posts')
            return redirect_url
        return super().get_redirect_url()