from django.contrib import admin

from .domain.models import Comment


admin.site.register(Comment)