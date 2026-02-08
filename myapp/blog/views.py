from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
import logging
from django.http import Http404
from .models import Post , Category, AboutUs
from django.core.paginator import Paginator
from .forms import ContactForm


# Create your views here.
def index(request):
    blog_title = "Latest Posts"
    all_posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(all_posts, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'blog_title': blog_title, 'page': posts})

def detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(Category=post.Category).exclude(pk=post.id)[:3]
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    # logger = logging.getLogger("Testing")
    # logger.debug(f'post variable content: {post}')
    return render(request, 'blog/detail.html', {'post': post, 'related_posts': related_posts})

def old_url_redirect(request):
    return redirect(reverse("blog:new_url_view"))

def new_url_view(request):
    return HttpResponse("This is the new URL view.")

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if form.is_valid():
            logger = logging.getLogger("Testing")
            logger.debug(f'POST data: {form.cleaned_data["email"]}')
            sucess_message = "Thank you for your message! We will get back to you soon."
            return render(request, 'blog/contact.html', {'form': form, 'success_message': sucess_message})
        else:
            logger = logging.getLogger("Testing")
            logger.debug(f'Form errors: {form.errors}')
        return render (request, 'blog/contact.html', {'form': form,'name': name, 'email': email, 'message': message})
    
    return render(request, 'blog/contact.html')
def about_view(request):
    about_content = AboutUs.objects.first().content
    return render(request, 'blog/about.html', {'about_content': about_content})