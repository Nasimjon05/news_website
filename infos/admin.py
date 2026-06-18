from django.contrib import admin
from .models import News,Category, Contact
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created', 'status')
    list_filter = ('status', 'created', 'updated')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created'
    search_fields = ('title',)
    ordering = ('-created',)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('fname','lname', 'email','text')

