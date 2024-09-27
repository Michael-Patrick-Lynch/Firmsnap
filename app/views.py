from django.http import HttpResponse
from django.template import loader
from .models import Post, Comment
from django.shortcuts import get_object_or_404



def index(request):
    return HttpResponse("Hello, world. You're at the app index.")

def post_detail(request, post_id):
    post_obj = get_object_or_404(Post, id=post_id)
    list_of_comments = Comment.objects.all()
    template = loader.get_template("app/post_detail.html")
    context = {"post_obj" : post_obj, "list_of_comments": list_of_comments}
    return HttpResponse(template.render(context, request))

# All posts for a specific organisation
def all_posts(request, organisation_id):
    list_of_posts = Post.objects.filter(organisation_id=organisation_id)
    template = loader.get_template("app/all_posts.html")
    context = {"list_of_posts": list_of_posts}
    return HttpResponse(template.render(context, request))
