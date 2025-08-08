from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

# posts = [
#     {
#         'title': 'Lagos is a beast',
#         'author': 'Prof. Adewale',
#         'date_posted': 'August 22, 2000',
#         'comment': 'I believe so much in Lagos that I will always leave here'
#     },
#     {
#         'title': 'My home',
#         'author': 'Mr Frank',
#         'date_posted': 'July 31, 2000',
#         'comment': 'We are alwaays at home'
#     }
# ]


# Create your views here.
def home(request):
    context = {
        'my_post': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Page'})
