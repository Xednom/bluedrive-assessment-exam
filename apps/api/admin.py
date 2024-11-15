from django.contrib import admin

from apps.api.models import Post, Comment, Author

# Register your models here.


class PostComment(admin.TabularInline):
    model = Comment
    extra = 1
    fields = ["content"]


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ("title", "published_date", "created_at")
    list_filter = ("title", "published_date", "created_at")
    search_fields = ("title", "published_date", "created_at")
    inlines = [PostComment]


class AuthorAdmin(admin.ModelAdmin):
    model = Author
    list_display = ("name", "email", "created_at")
    list_filter = ("name", "email", "created_at")
    search_fields = ("name", "email", "created_at")


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
