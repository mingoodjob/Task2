from django.contrib import admin
from .models import ProductModel, ReviewModel

class ReviewInline(admin.TabularInline):
    model = ReviewModel
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title','thumnail', 'price')
    list_display_links = ('title',)
    list_filter = ('author', 'title')
    search_fields = ('title', 'desc',) 
    fieldsets = (
        ("정보", {'fields': ('author', 'title', 'desc', 'thumnail', 'price')}),
        ("게시", {'fields': ('exposure_start', 'exposure_end', 'active')}),
        ("등록일", {'fields': ('created_at', 'updated_at',)}),
    )

    filter_horizontal = []
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('author', 'created_at', 'updated_at',)
        else:
            return ('created_at', 'updated_at',)

    inlines = [
        ReviewInline,
    ]
    
admin.site.register(ProductModel, ProductAdmin)
admin.site.register(ReviewModel)
