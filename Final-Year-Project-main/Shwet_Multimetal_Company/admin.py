from django.contrib import admin
from Shwet_Multimetal_Company.models import  Product, Category, ProductImages, Review, Contact, UserDetails

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['id' ,'user', 'title', 'product_image', 'price', 'featured', 'product_status']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id' ,'title', 'category_image']

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'content', 'address', 'timestamp')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'content', 'created_at')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Review, ReviewAdmin)
