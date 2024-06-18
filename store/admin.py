from .models import *
from tags.models import TaggedItem
from django.db.models import Count
from django.contrib import admin
from django.utils.html import format_html 
from django.utils.http import urlencode
from django.contrib.contenttypes.admin import GenericTabularInline
from django.urls import reverse

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    search_fields = ['title']
    autocomplete_fields = ['featured_product']

    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({'collection_id': str(collection.id)})
        )
        return format_html('<a href="{}">{}</a>', url, collection.products_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('products')
        
        )
###################################################    

class Media:
    css = {
        'all':['store/style.css']
    }

###################################################
class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem

###################################################

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    readonly_fields = ['thumbnail']
    def thumbnail(self,instance):
        if instance.image.name != '':
            return format_html(f'<img src = "{instance.image.url}" class= "thumbnail"/>')
        return ''
    

###################################################
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields= ['collection']
    inlines = [ProductImageInline]
    list_display = ['title', 'price','inventory_status','collection']
    inlines = [TagInline]
    list_editable = ['price']
    list_select_related = ['collection']
    list_filter = ['collection']
    search_fields = ['title']

    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'
####################################################    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'product','description' ,'date']
    search_fields = ['name', 'product__title']
    list_filter = ['date']
####################################################
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'membership']
    list_select_related = ['user']
    list_editable = ['membership']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
    autocomplete_fields = ['user']
####################################################
class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display = ['placed_at', 'payment_status', 'customer']

####################################################
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']

####################################################
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['street', 'city', 'customer']

####################################################
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['created_at']

####################################################
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity']                        