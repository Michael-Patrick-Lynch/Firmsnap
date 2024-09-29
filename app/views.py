import logging
from django.http import HttpResponse
from django.template import loader
from .models import Post, Comment
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.views import LoginView
from django.urls import reverse

def index(request):
    return HttpResponse("Hello, world. You're at the app index.")

def post_detail(request, post_id):
    post_obj = get_object_or_404(Post, id=post_id)
    list_of_comments = Comment.objects.filter(post_id=post_id)
    template = loader.get_template("app/post_detail.html")
    context = {"post_obj" : post_obj, "list_of_comments": list_of_comments}
    return HttpResponse(template.render(context, request))

# All posts for a specific organisation
def all_posts(request, organisation_id):
    list_of_posts = Post.objects.filter(organisation_id=organisation_id)
    return render(request, "app/all_posts.html", {"list_of_posts": list_of_posts})

# This is needed so that users are directed to the feed for
# their org as soon as they log in
class CustomLoginView(LoginView):
    def get_redirect_url(self):
        user = self.request.user

        # If the login is not working, it could be because the user has no org id!!
        if user.is_authenticated and user.organisation_id:
            org_id = user.organisation_id.id
            redirect_url = reverse('all_posts', kwargs={'organisation_id': org_id})
            return redirect_url
        return super().get_redirect_url()