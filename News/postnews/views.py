from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView,
	)

from .models import Author, Post, Category
from .filters import PostFilter
from .forms import PostForm
from datetime import datetime
from django.urls import reverse_lazy

# Create your views here.


class PostMany(ListView):

	model = Post
	ordering = '-time_create'
	template_name = 'post_one.html'
	context_object_name = 'post'
	# Вывод не более 10 новостей
	paginate_by = 10

	def get_queryset(self):

		queryset = super().get_queryset()
		self.filterset = PostFilter(self.request.GET, queryset)

		return self.filterset.qs

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)
		context['filterset'] = self.filterset

		return context

class CategoryMany(ListView):
	model = Category
	ordering = 'name'
	template_name = 'category_many.html'
	context_object_name = 'categoryes'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['time_now'] = datetime.utcnow()
		context['next_sale'] = None
		return context

# Представление поиска постов
class PostSearch(ListView):

	model = Post
	template_name = 'news_search.html'
	context_object_name = 'post_search'

	def get_queryset(self):

		queryset = super().get_queryset()
		self.filterset = PostFilter(self.request.GET, queryset)

		return self.filterset.qs

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)
		context['filterset'] = self.filterset

		return context

# Представления 'Новости'
class NewsCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
	permissions_requred = ('news.create_new')
	form_class = PostForm
	model = Post
	template_name = 'news_create.html'

	def form_valid(self, form):
		news = form.save(commit=False)
		news.post_or_new = 'Новость'
		return super().form_valid(form)

class NewsDetail(DetailView):

	model = Post
	template_name = 'news_detail.html'
	context_object_name = 'news'

class NewsEdit(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
	permissions_requred = ('news.edit_new')

	form_class = PostForm
	model = Post
	template_name = 'news_edit.html'

class NewsDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
	permissions_requred = ('news.del_new')

	model = Post
	template_name = 'news_delete.html'
	success_url = reverse_lazy('post_list')



# Представления 'Статьи'
class ArticlesCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
	permissions_requred = ('news.art_create')

	form_class = PostForm
	model = Post
	template_name = 'articles_create.html'

	def form_valid(self, form):
		articles = form.save(commit=False)
		articles.post_or_new = 'Статья'
		return super().form_valid(form)

class ArticlesDetail(DetailView):

	model = Post
	template_name = 'articles_detail.html'
	context_object_name = 'articles'

class ArticlesEdit(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
	permissions_requred = ('news.art_edit')

	form_class = PostForm
	model = Post
	template_name = 'articles_edit.html'

class ArticlesDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
	permissions_requred = ('news.art_del')

	model = Post
	template_name = 'articles_delete.html'
	success_url = reverse_lazy('post_list')


