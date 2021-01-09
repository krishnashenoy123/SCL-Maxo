from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
# from .models import Files
import pyrebase


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'focus/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'focus/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'focus/about.html', {'title': 'About'})

# class PostUploadView(DetailView):
#     model = Files
#     fields = ['names', 'content']

#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False

#     config={
#             'apiKey': "AIzaSyDLzBjNqg37fRiCBClXzamhjdVN2jr4nX8",
#             'authDomain': "fir-9f329.firebaseapp.com",
#             'databaseURL':"https://fir-9f329.firebaseio.com",
#             'projectId': "fir-9f329",
#             'storageBucket': "fir-9f329.appspot.com",
#             'messagingSenderId': "1022042387286",
#             'appId': "1:1022042387286:web:efbafb88c136023dd0dcf7",
#             'measurementId': "G-F8NR0833P8"
#             }
#     firebase= pyrebase.initialize_app(config)
#     storage=firebase.storage()
#     path_local= names
    
#     path_on_cloud = post.id+'/'
#     storage.child(path_on_cloud).put(path_local)
#     Url=storage.child(path_on_cloud).get_url(None)
#     print(Url)




