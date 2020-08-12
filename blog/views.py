from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'NadineL',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 12, 2020'
    },
    {
        'author': 'Elon Musk',
        'title': 'Blog Post 12',
        'content': 'Second post content',
        'date_posted': 'August 13, 2020'
    },
]

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
     return render(request, 'blog/about.html', {'title': 'About'})