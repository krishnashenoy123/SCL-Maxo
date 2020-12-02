from django.shortcuts import render
# Create your views here.
# posts= [
#     {
#         'author':'Rishabh',
#         'title':'blog-post1',
#         'content':'First post',
#         'date_posted':'August 27, 2018'
#     },
#     {
#         'author':'Hrishi',
#         'title':'blog-post2',
#         'content':'Second post',
#         'date_posted':'August 29, 2018'
#     }

# ]


def home(request):
    # context = {
    #     'posts':posts
    # }
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})

def register(request):
    return render(request, 'blog/register.html',{'title':'Register'})

def login(request):
    return render(request, 'blog/login.html',{'title':'Login'})


