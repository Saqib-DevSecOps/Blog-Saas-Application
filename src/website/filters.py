import django_filters
from django.db.models import Q
from django.forms import TextInput, ModelForm
from src.website.models import BlogCategory, Blog, Comment


class BlogFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label=''
                                      , widget=TextInput(attrs={'placeholder': 'Search Blogs here',
                                                                'class': 'form-control rounded-pill'}),
                                      method='blog_filter')

    class Meta:
        model = Blog
        fields = ['title', ]

    def blog_filter(self, queryset, name, value):
        return queryset.filter(Q(title__icontains=value) | Q(meta_title__icontains=value, description__icontains=value))


class CommentsForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comments'
        ]
