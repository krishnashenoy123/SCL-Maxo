from django.shortcuts import render
# Create your views here.
posts= [
    {
        'author':'Rishabh',
        'title':'blog-post1',
        'content':'First post',
        'date_posted':'August 27, 2018'
    },
    {
        'author':'Hrishi',
        'title':'blog-post2',
        'content':'Second post',
        'date_posted':'August 29, 2018'
    }

]


def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})


