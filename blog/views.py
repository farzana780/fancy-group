from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm,EditForm

# def LikeView(request,pk):
#     post =get_object_or_404(Post, id=request.POST.get('post_id'))
#     liked = False
#     if post.likes.filter(id=request.user.id).exists():
#         post.likes.remove(request.user)
#         liked = False
#     else:
#         post.likes.add(request.user)
#         liked = True
#     return HttpResponseRedirect(reverse('blog:blogdetails', args=[str(pk)]))


class Bloghome(ListView):
    model = Post
    template_name = 'blog/blog.html'
    ordering = ['id']
    paginate_by = 2


class Blogdetails(DetailView):
    model = Post
    template_name = 'blog/blogdetails.html'

    # def get_context_data(self, **kwargs):
    #     context = super(Blogdetails, self).get_context_data(**kwargs)
    #     stuff = get_object_or_404(Post, id=self.kwargs['pk'])
    #     total_likes = stuff.total_likes()
    #
    #     liked = False
    #     if stuff.likes.filter(id=self.request.user.id).exists():
    #         liked = True
    #     context ["total_likes"] = total_likes
    #     context["liked"] = liked
    #     return context


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'


class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "blog/update_post.html"


class DeletePost(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:bloghome')
