from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):
    if request.method=="POST":
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
     # Get all posts, limit = 20
    posts = Post.objects.all()[:20]
    
    #Show
    return render(request,'posts.html',
                     {'posts': posts})



def delete(request,post_id):
    post=Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect("/")
    

def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("not valid")
    form = PostForm
    return render(request, 'edit.html', {'post': post, 'form': form})

def likeview(request, post_id):
    new_value=Post.objects.get(id =post_id)
    new_value.likes +=1
    new_value.save()
    return HttpResponseRedirect('/')
