from .views import *
from django.urls import path
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products',ProductViewSet,basename='products')
router.register('collections',CollectionViewSet)
router.register('carts',CartViewSet)
router.register('customers',CustomerViewSet,basename='customers')
router.register('orders',OrderViewSet,basename='orders')

products_router =  routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews',ReviewViewSet,basename='product-reviews')
products_router.register('images',ProductImageViewSet,basename='product-images')

carts_router = routers.NestedDefaultRouter(router,'carts',lookup='cart')
carts_router.register('items',CartItemViewSet,basename='cart-items')


urlpatterns = router.urls + products_router.urls + carts_router.urls

