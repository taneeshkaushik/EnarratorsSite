from django.contrib import admin
from .models import Article
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Article)