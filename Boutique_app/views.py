from django.shortcuts import render
from django.views import View

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'Boutique_app/index.html')


class Search(View):
    def get(self, request):
        return render(request, 'Boutique_app/index.html')
    



# Autres vues de base
def about(request):
    return render(request, 'Boutique_app/about.html')

def category(request):
    return render(request, 'Boutique_app/category.html')

def product_details(request, id=None):
    return render(request, 'product_details.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'Boutique_app/contact.html')

def faq(request):
    return render(request, 'faq.html')

def blog(request):
    return render(request, 'blog.html')

def featured_products(request):
    return render(request, 'featured.html')

def new_arrivals(request):
    return render(request, 'new_arrivals.html')

def sale_items(request):
    return render(request, 'sale.html')

def search(request):
    return render(request, 'search.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def logout_view(request):
    return render(request, 'logout.html')

def account(request):
    return render(request, 'account.html')

def orders(request):
    return render(request, 'orders.html')