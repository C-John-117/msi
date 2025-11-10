from django.urls import path
from . import views

app_name = 'Boutique_app'

urlpatterns = [
    path('', views.Home.as_view(), name='Home'),

    #url de recherhe de produits search
    #url des comptes  account
    #url des commandes orders
    #url de deconnection logout
    #url de produits likés whishlist
    #url du panier actuel cart

    path('', views.Home.as_view, name='home'),
    path('about/', views.about, name='about'),
    path('category/', views.category, name='category'),
    #path('product/<int:id>/', views.product_details, name='product_details'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('featured/', views.featured_products, name='featured_products'),
    path('new/', views.new_arrivals, name='new_arrivals'),
    path('sale/', views.sale_items, name='sale_items'),
    path('search/', views.Search.as_view(), name='Search'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('account/', views.account, name='account'),
    path('orders/', views.orders, name='orders'),
]
