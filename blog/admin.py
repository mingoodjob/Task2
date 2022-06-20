from django.contrib import admin
from blog.models import Category, Article, Comment
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    list_display_links = ('name', )
    list_filter = ('name', )
    search_fields = ('name', )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author','date',)
    list_display_links = ('title', )
    list_filter = ('id', 'title', 'category', 'author', 'date', )
    search_fields = ('title', 'content', 'author', )

    fieldsets = (
        ("정보", {'fields': ('title', 'author', 'content')}),
        ("카테고리", {'fields': ('category', )}),
        ("노출시간", {'fields': ('exposure_start','exposure_end', )}),
        )

    filter_horizontal = ['category',]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('author', 'date',)
        else:
            return ('date',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)