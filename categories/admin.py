from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from categories.models import Category


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    pass
