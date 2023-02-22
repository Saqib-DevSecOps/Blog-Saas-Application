from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from src.website.filters import BlogFilter
from src.website.models import Blog, BlogCategory, Comment


# Create your views here.


def home(request):
    print(request.tenant.domain_url)
    return HttpResponse("ok")


class Blogs(ListView):
    model = Blog
    paginate_by = 10
    template_name = 'website/blog.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Blogs, self).get_context_data(**kwargs)
        category = self.request.GET.get('category')
        print(category)

        if category and self.request is not None:
            blog = Blog.objects.filter(category__id=category)
        else:
            blog = Blog.objects.all().order_by('views', '-created_at')
        context['recent'] = Blog.objects.all().order_by('-created_at')[:4]
        filter_blogs = BlogFilter(self.request.GET, queryset=blog)
        pagination = Paginator(filter_blogs.qs, 10)
        page_number = self.request.GET.get('page')
        print(page_number)
        page_obj = pagination.get_page(page_number)
        context['blogs_category'] = BlogCategory.objects.all()
        context['blogs'] = page_obj
        context['filter_form'] = filter_blogs
        context['category'] = category
        return context


class BlogDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        comments = Comment.objects.filter(blog_id=pk)
        blog = Blog.objects.get(id=pk)
        blog.views += 1
        blog.save()
        context = {'comments': comments, 'object': blog}
        return render(self.request, 'website/blog_details.html', context)

    @method_decorator(login_required, name='dispatch')
    def post(self, request, pk, *ars):
        blog = Blog.objects.get(id=pk)
        comment = request.POST.get('comment')
        data = Comment.objects.create(
            user=self.request.user,
            blog=blog,
            comments=comment,
        )
        data.save()
        return redirect('website:blog-detail', pk)
