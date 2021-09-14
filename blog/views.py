from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author': 'Revanth',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 13, 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 13, 2021'

    }


]



def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})


